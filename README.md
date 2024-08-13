# 🏠🏢 Deployment project

## 📜 Description


This repository contains a web application where I have implemented a Random Forest model, serialized it using pickle, 
and compressed it using joblib. The backend of the project is powered by FAST API, and the frontend is developed with Streamlit.
The model is deployed on Streamlit, while the FastAPI is deployed on Render. The integration between the FastAPI backend 
and the Streamlit frontend is accomplished using the requests library. 

This web application is designed to predict the price of a house based on user-provided inputs. 
The link to the deployed project is provided in the description.



## 📦 Installation
 
- To run this project, you need to have Python installed on your machine.
  You also need the following Python libraries:

- `numpy`

- `sklearn`

- `fastapi`

- `pandas`

- `PIL`

- `streamlit`

- `requests`


## 🛠️ Project Structure

	•	model_rf.pkl/ - This directory contains the serialized Random Forest model.
	•	main.py/ - Contains the FastAPI application files.
	•	streamlit_app/ - Contains the Streamlit frontend application files.
	•	requirements.txt - A list of all the dependencies required to run the project.
	•	dockerfile - A list of commands for Render's deployment.


## 👥 Contributors

Alisher Jardemaliyev 


## 📅 Timeline

- `Day 1`: Data Preprocessing and Integration

- `Day 2`: Development of Backend Components using FAST API

- `Day 3`: Implementation, and Integration with Frontend (Streamlit)

- `Day 4`: Deployment and Final Touches