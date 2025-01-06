#!/usr/bin/env python
# coding: utf-8

# In[17]:


import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import Workbook

def scrape_course_details(page_url):
    response = requests.get(page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    courses = []
    
    course_containers = soup.find_all('a', class_='course-card course-card__public published')
    for container in course_containers:
        course_data = {
            'course_name': '',
            'course_url': '',
            'lesson_count': '',
            'price': '',
            'description': '',
            'instructor': '',
            'rating': '',
            'difficulty_level': ''
        }
        
        # Basic Details from list page
        course_name_elem = container.find('h3')
        if course_name_elem:
            course_data['course_name'] = course_name_elem.get_text(strip=True)
        
        course_data['course_url'] = 'https://courses.analyticsvidhya.com' + container['href']
        
        lesson_count_elem = container.find('span', class_='course-card__lesson-count')
        if lesson_count_elem:
            course_data['lesson_count'] = lesson_count_elem.find('strong').get_text(strip=True) if lesson_count_elem.find('strong') else ''
        
        price_elem = container.find('span', class_='course-card__price')
        if price_elem:
            course_data['price'] = price_elem.find('strong').get_text(strip=True) if price_elem.find('strong') else ''
        
        # Fetch detailed information from the course page
        detail_response = requests.get(course_data['course_url'])
        detail_soup = BeautifulSoup(detail_response.text, 'html.parser')
        
        # Description
        description_section = detail_soup.find('section', class_='rich-text')
        if description_section:
            description_content = description_section.find('div', class_='fr-view')
            if description_content:
                course_data['description'] = description_content.get_text(strip=True)

        # Instructor
        instructor_sections = detail_soup.find_all('section', class_='text-image__body')
        for section in instructor_sections:
            instructor_name = section.find('h4', class_='section__subheading')
            if instructor_name:
                course_data['instructor'] = instructor_name.get_text(strip=True).split(' - ')[0]
                break
        
        # Additional Info (Duration, Rating, Difficulty Level)
        info_section = detail_soup.find('section', class_='text-icon')
        if info_section:
            for item in info_section.find_all('li', class_='text-icon__list-item'):
                icon = item.find('i')
                if icon:
                    if 'fa-star' in icon['class']:
                        course_data['rating'] = item.find('h4').get_text(strip=True)
                    elif 'fa-signal' in icon['class']:
                        course_data['difficulty_level'] = item.find('h4').get_text(strip=True)
        
        courses.append(course_data)

    return courses

def main():
    base_url = "https://courses.analyticsvidhya.com/collections/courses"
    all_courses = []

    for page in range(1, 10):  # Assuming there are 9 pages
        if page > 1:
            page_url = f"{base_url}?page={page}"
        else:
            page_url = base_url
        
        courses_on_page = scrape_course_details(page_url)
        all_courses.extend(courses_on_page)

    # Write to CSV
    with open('courses_detailed.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['course_name', 'course_url', 'lesson_count', 'price', 'description', 'instructor', 'rating', 'difficulty_level'])
        writer.writeheader()
        for course in all_courses:
            writer.writerow(course)
    
    # Write to Excel
    wb = Workbook()
    ws = wb.active
    ws.append(['course_name', 'course_url', 'lesson_count', 'price', 'description', 'instructor', 'rating', 'difficulty_level'])
    
    for course in all_courses:
        ws.append([course['course_name'], course['course_url'], course['lesson_count'], 
                   course['price'], course['description'], course['instructor'], 
                   course['rating'], course['difficulty_level']])

    wb.save('courses_detailed_excel.xlsx')

if __name__ == "__main__":
    main()

