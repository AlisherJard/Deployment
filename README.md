# 🏠🏢 Deployment project

## 📜 Description


This repository contains a web application where I have implemented a Random Forest model, serialized it using pickle, 
and compressed it using joblib. The backend of the project is powered by FastAPI, and the frontend is developed with Streamlit.
The model is deployed on Streamlit, while the FastAPI is deployed on Render. The integration between the FastAPI backend 
and the Streamlit frontend is accomplished using the requests library. 

This web application is designed to predict the price of a house based on user-provided inputs. 
The link to the deployed project is provided in the description or [here](https://alisherjard-deployment-streamlit-app-jpegcx.streamlit.app).



## 📦 Installation
 
- To run this project, you need to have Python installed on your machine.
  You also need the following Python libraries:

![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![PIL](https://img.shields.io/badge/PIL-5C2D91?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Requests](https://img.shields.io/badge/requests-3776AB?style=for-the-badge&logo=python&logoColor=white)


## 🛠️ Project Structure

	•	model_rf.pkl - This directory contains the serialized Random Forest model.
	•	main.py - Contains the FastAPI application files.
	•	streamlit_app - Contains the Streamlit frontend application files.
	•	requirements.txt - A list of all the dependencies required to run the project.
	•	dockerfile - A list of commands for Render's deployment.
	•	model_test.py - The R2 and Mean Absolute Error (MAS) results for the model_rf.pkl
	•	cleaned_data.csv - Complete dataset (X_train + X_test + target)
	•	X_test.csv - 20% of training data of cleaned_data.csv 

## 👐 Usage

Step 1: Visit the Web Application

Head over to the provided URL https://alisherjard-deployment-streamlit-app-jpegcx.streamlit.app

Step 2: Input House Parameters

Once you’re on the site, you will be prompted to input the parameters of the house you wish to evaluate. These parameters typically include:

	•	Location: Enter the city or neighborhood.
	•	Number of Bedrooms: Specify the number of bedrooms.
	•	Number of Bathrooms: Specify the number of bathrooms.
	•	Square Footage: Enter the total square footage of the house.
	•	Year Built: Provide the year the house was constructed.
	•	Other Features: Additional details such as the presence of a flooding zone, PEB or equipped kitchen.

Step 3: Get the Prediction

After entering the necessary information, submit the form. The application will process the input data and provide a prediction for the house value.

Step 4: Review Predictor Performance

To understand how the predictor works, you can check its performance on other datapoints:

	•	Historical Data: Review how the model performed on similar properties.
	•	Comparative Analysis: See how the prediction compares with actual market data.

Step 5: Download Test Data

If you want to dive deeper into the model’s performance or test it with other data, you can download the test dataset directly from the platform. This can be useful for analysis, experimentation, or further validation.


## 👥 Contributors

Alisher Jardemaliyev 


## 📅 Timeline

- `Day 1`: Data Preprocessing and Integration

- `Day 2`: Development of Backend Components using FAST API

- `Day 3`: Implementation, and Integration with Frontend (Streamlit)

- `Day 4`: Deployment and Final Touches