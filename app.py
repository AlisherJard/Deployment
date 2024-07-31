# from fastapi import FastAPI
# import os
#
# # Set port to the env variable PORT to make it easy to choose the port on the server
# # If the Port env variable is not set, use port 8000
# PORT = os.environ.get("PORT", 8000)
# app = FastAPI(port=PORT)
#
#
#
# @app.get("/")
# async def root():
#     """Route that return 'Alive!' if the server runs."""
#     return {"MAGA": "Alive!"}
#
#
# @app.get("/hello")
# async def say_hello(user: str = "Anonymous"):
#     """Route that will return 'hello {user}'."""
#     return {"Message": f"Hello {user}!"}

from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
import pickle
from sklearn.metrics import mean_absolute_error
import numpy as np


df_pd = pd.read_csv("cleaned_data.csv")
features = []
features = df_pd.drop(['Price'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(features, np.log(df_pd['Price']),test_size=0.2, random_state=0)


# joblib.dump(rfr_model, 'model_rf.pkl', compress=9)
loaded_model = joblib.load('model_rf.pkl')

# Predict and evaluate
y_pred = loaded_model.predict(X_test)

score = loaded_model.score(X_test, y_test)
mae = mean_absolute_error(np.exp(y_test), np.exp(y_pred))

print(f"Model Score: {score}")
print(f"Model MAE: {mae}")