# **Smart Search Tool for Free Courses on Analytics Vidhya**

### **Overview**
This project is a smart search tool designed to help users find the most relevant free courses on Analytics Vidhya’s platform. It utilizes natural language processing (NLP) and vector embeddings to deliver accurate course recommendations based on user queries. The tool is deployed on Hugging Face Spaces for public access.

---

## **Features**
- **Semantic Search**: Quickly finds courses based on keywords and natural language queries.  
- **Web Scraping**: Extracted comprehensive course data (titles, descriptions, instructors, etc.) from Analytics Vidhya’s platform.  
- **NLP-Powered Recommendations**: Uses embeddings to rank and retrieve the most relevant courses.  
- **Interactive UI**: A user-friendly interface built using Gradio for seamless search experience.  
- **Deployment**: Fully deployed and accessible on Hugging Face Spaces.  

---

## **Tech Stack**
- **Programming Language**: Python  
- **Web Scraping**: BeautifulSoup, Requests  
- **NLP**: Sentence Transformers (`all-MiniLM-L6-v2`), LangChain 0.3.x / LlamaIndex 0.12.x  
- **Vector Database**: FAISS / ChromaDB  
- **Frontend**: Gradio  
- **Deployment**: Hugging Face Spaces  

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/Sahilsingh75/Smart-Search-Tool-for-Free-Courses-on-Analytics-Vidhya
cd Smart-Search-Tool-for-Free-Courses-on-Analytics-Vidhya
```

### **2. Set Up the Environment**
- Install Python dependencies:
  ```bash
  pip install -r requirements.txt
  ```

- Ensure the following libraries are included in `requirements.txt`:
  ```text
  beautifulsoup4
  requests
  pandas
  numpy
  sentence-transformers
  faiss-cpu
  gradio
  langchain==0.3.x
  llama-index==0.12.x
  ```

### **3. Run Locally**
- To start the application locally:
  ```bash
  python app_analytics_vidhya_smart_search_system.py
  ```
- Open the URL displayed in the terminal to interact with the search tool.

---

## **Usage**
1. Visit the [Hugging Face Space Link](https://huggingface.co/spaces/sahil7505/smartcoursesearch).  
2. Enter a keyword or natural language query (e.g., "data analysis courses") in the search bar.  
3. The tool will return a list of the most relevant free courses, including the course name, description, and a link to the course page.

---

## **Dataset**
The course data was collected by scraping Analytics Vidhya’s free courses pages. The `scraper.py` script is included in this repository for reference. Key details include:  
- **Fields**: Course name, URL, description, instructor, rating, difficulty level, lesson count.  
- **Data Files**:  
  - `courses_detailed.csv`: Contains the scraped dataset.
  - `cleaned_courses.csv`: Contains the cleaned dataset.   

---

## **Project Structure**
```
smart-search-analytics-vidhya/
├── app_analytics_vidhya_smart_search_system.py      # Main application script
├── scraper.py                                       # Script to scrape course data
├── courses_detailed.csv                             # Scraped course data
├── cleaned_courses.csv                              # cleaned data file
├── app_analytics_vidhya_smart_search_system.ipynb  # Main application notebook
├── scraper.ipynb                                   # Notebook to scrape course data
├── requirements.txt                                 # Python dependencies
├── README.md                                        # Project documentation
├── LICENSE                                          # License file 
```

---

## **Live Demo**
Check out the live demo on Hugging Face Spaces:  
[**Smart Search Tool for Free Courses**](https://huggingface.co/spaces/sahil7505/smartcoursesearch)

---

## **Methodology**
A detailed explanation of the project approach, including data collection, embedding generation, and deployment, is available in the accompanying documentation file (`methodology.pdf`).

---

## **Contributing**
Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request. Ensure your changes are well-documented.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

## **Acknowledgments**
- [Analytics Vidhya](https://courses.analyticsvidhya.com/collections/courses) for providing an excellent platform to explore data science resources.
- [Hugging Face](https://huggingface.co/) for hosting the deployment.
- OpenAI for providing powerful tools like LangChain and Sentence Transformers.

