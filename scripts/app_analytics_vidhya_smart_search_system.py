#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Load the CSV file
file_path = 'data/courses_detailed.csv' 
data = pd.read_csv(file_path)

# Clean and preprocess data
data['lesson_count'] = data['lesson_count'].fillna('Unknown')
data['instructor'] = data['instructor'].fillna('Unknown')
data['rating'] = data['rating'].fillna('0/5')
data['difficulty_level'] = data['difficulty_level'].fillna('Unknown')

# Normalize text data
data['course_name'] = data['course_name'].str.lower()
data['description'] = data['description'].str.lower()

# Combine text fields for embedding
data['text'] = data['course_name'] + " " + data['description']

# Save cleaned data
data.to_csv('cleaned_courses.csv', index=False)
print("Data cleaned and saved.")


# In[3]:


from sentence_transformers import SentenceTransformer

# Load a pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for the combined text field
embeddings = model.encode(data['text'].tolist(), convert_to_tensor=True)

print(f"Generated embeddings with shape: {embeddings.shape}")


# In[5]:


import faiss

# Initialize FAISS index
d = embeddings.shape[1]  # Dimension of embeddings
faiss_index = faiss.IndexFlatL2(d)  # Use L2 similarity
faiss_index.add(embeddings.cpu().numpy())  # Add embeddings to FAISS index

print(f"FAISS index built with {faiss_index.ntotal} items.")


# In[7]:


def search_courses(query, data, top_k=5):
    # Generate an embedding for the query
    query_embedding = model.encode([query], convert_to_tensor=True).cpu().numpy()
    
    # Search using FAISS
    distances, indices = faiss_index.search(query_embedding, top_k)
    
    # Retrieve course details
    results = data.iloc[indices[0]]
    results['distance'] = distances[0]
    
    return results[['course_name', 'course_url', 'description', 'rating', 'difficulty_level', 'distance']].to_dict('records')


# In[9]:


import gradio as gr

def gradio_search_interface(query, top_k=5, min_rating=0):
    # Get results
    results = search_courses(query, data, top_k)
    
    # Apply rating filter
    filtered_results = [
        result for result in results if float(result['rating'].split('/')[0]) >= min_rating
    ]
    
    # Format results for display
    formatted_results = "\n\n".join([
        f"**Course Name:** {result['course_name'].title()}\n"
        f"**Description:** {result['description']}\n"
        f"**Rating:** {result['rating']}\n"
        f"**Difficulty Level:** {result['difficulty_level']}\n"
        f"**Distance:** {result['distance']:.4f}\n"
        f"[Course Link]({result['course_url']})" for result in filtered_results
    ])
    
    return formatted_results or "No courses found matching your criteria."

# Define Gradio interface
iface = gr.Interface(
    fn=gradio_search_interface, 
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter your search query here..."), 
        gr.Slider(1, 10, step=1, label="Number of Results"), 
        gr.Slider(0.0, 5.0, step=0.5, label="Minimum Rating")
    ], 
    outputs="markdown",
    title="Smart Course Search Tool",
    description="Search for courses by entering keywords. Filter results by number of results and minimum rating."
)

# Launch Gradio interface
iface.launch()

