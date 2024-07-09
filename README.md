# resume_classifier
NLP Model to classify multiple PDF resumes into job categories.

# Project Description

This project focuses on developing a machine learning model that classifies resumes into predefined job categories. The model leverages a collection of resume examples to predict the category of a given resume. The training data for this project has been sourced from Kaggle.

After building and evaluating multiple models, the best performing one has been deployed as a web application. This application allows users to upload multiple resumes and receive predicted categories for each resume. Additionally, the app provides a pie chart visualizing the distribution of different categories among the uploaded resumes, offering an intuitive overview of the classification results.

# Data Definition

The training dataset contains over 2400 resumes in both string and PDF formats. The data is organized in the following manner:

- **PDFs:** Stored in the data folder, differentiated into their respective labels as subfolders. Each resume resides inside the folder in PDF form, with the filename as the ID defined in the CSV.
- **CSV:** Contains metadata about the resumes with the following columns:<br/>
  **ID:** Unique identifier and file name for the respective PDF. <br/>
  **Resume_str:** Contains the resume text in string format. <br/>
  **Resume_html:** Contains the resume data in HTML format as present while web scraping. <br/>
  **Category:** Category of the job the resume was used to apply for.<br/>
