import streamlit as st
import joblib
import fitz  # PyMuPDF
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import requests 
import os



# Load the model and vectorizer

# Function to download files from a URL
def download_file(url, dest_path):
    response = requests.get(url)
    with open(dest_path, 'wb') as file:
        file.write(response.content)

# URL of the .pkl file hosted on GitHub
model_url = 'https://github.com/j-poddar/resume_classifier/releases/download/model_classifier/resume_classifier.pkl'
# Download the model if it doesn't already exist
if not os.path.exists('resume_classifier.pkl'):
    download_file(model_url, 'resume_classifier.pkl')

# Load the model and vectorizer
model = joblib.load('resume_classifier.pkl')





vectorizer = joblib.load('vectorizer.pkl')

def extract_text_from_pdf(pdf_file):
    text = ""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

def preprocess_text(text):
    # Add any text preprocessing steps here if needed
    return text

def classify_resumes(uploaded_files):
    results = []
    for uploaded_file in uploaded_files:
        text = extract_text_from_pdf(uploaded_file)
        cleaned_text = preprocess_text(text)
        features = vectorizer.transform([cleaned_text])
        prediction = model.predict(features)
        results.append((uploaded_file.name, prediction[0]))
    return results

# Streamlit app
st.title('Resume Categorization')
uploaded_files = st.file_uploader("Upload resumes in PDF format", type="pdf", accept_multiple_files=True)

if uploaded_files:
    with st.spinner('Classifying resumes...'):
        results = classify_resumes(uploaded_files)
        
        # Create a DataFrame to store the results
        df = pd.DataFrame(results, columns=['Resume_Title', 'Resume_Category'])
        
        # Display the results in a table
        st.write("### Classification Results")
        st.dataframe(df)
        
        # Display the results in a pie chart
        category_counts = df['Resume_Category'].value_counts()
        fig, ax = plt.subplots()
        ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        
        st.write("### Category Distribution")
        st.pyplot(fig)
