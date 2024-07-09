# resume_classifier
NLP Model to classify multiple PDF resumes into job categories.

# Project Description

This project focuses on developing a machine learning model that classifies resumes into predefined job categories. The model leverages a collection of resume examples to predict the category of a given resume. The training data for this project has been sourced from Kaggle.

After building and evaluating multiple models, the best performing one has been deployed as a web application. This application allows users to upload multiple resumes and receive predicted categories for each resume. Additionally, the app provides a pie chart visualizing the distribution of different categories among the uploaded resumes, offering an intuitive overview of the classification results.

# Data Definition

The training dataset contains over 2400 resumes in both string and PDF formats. The data is organized in the following manner:

- **PDFs:** Stored in the data folder, differentiated into their respective labels as subfolders. Each resume resides inside the folder in PDF form, with the filename as the ID defined in the CSV.
- **CSV:** Contains metadata about the resumes with the following columns:<br/>
   &nbsp; &nbsp; &nbsp; &nbsp; **ID:** Unique identifier and file name for the respective PDF. <br/>
   &nbsp; &nbsp; &nbsp; &nbsp; **Resume_str:** Contains the resume text in string format. <br/>
   &nbsp; &nbsp; &nbsp; &nbsp; **Resume_html:** Contains the resume data in HTML format as present while web scraping. <br/>
   &nbsp; &nbsp; &nbsp; &nbsp; **Category:** Category of the job the resume was used to apply for.<br/>

#### Present categories are: 
HR, Designer, Information-Technology, Teacher, Advocate, Business-Development, Healthcare, Fitness, Agriculture, BPO, Sales, Consultant, Digital-Media, Automobile, Chef, Finance, Apparel, Engineering, Accountant, Construction, Public-Relations, Banking, Arts, Aviation.

# Web Application
PUT SCREENSHOT HERE

The web application allows users to upload multiple resumes and get predictions for each. The application can be accessed [from here](https://resumeclassifier-jp.streamlit.app).<br/>
#### The app features:

- **Upload Button:** For users to upload multiple resume files. The user can test with few sample resumes available [here].
- **Predict Button:** To start the prediction process.
- **Results Display:** Shows the uploaded files and their predicted categories.
- **Pie Chart:** Visualizes the distribution of categories among the uploaded resumes.

## Web App Usage
1. Upload resume files using the upload button.
   
2. Click the predict button to start the prediction process.
3. View the predicted categories and the pie chart of the category distribution.


## Acknowledgements
- This project uses [Streamlit](https://streamlit.io) to build the web interface, and [Streamlit Community Cloud](https://streamlit.io/cloud) to deploy the web application.
- Thanks to [Kaggle](https://www.kaggle.com) for providing the [resume dataset](https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset/data).

