from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from fastapi.responses import FileResponse

# Loading of the trained model
loaded_model = joblib.load('model_rf.pkl')

app = FastAPI()

# Defining the Features class to match our dataset's structure
class Features(BaseModel):
    District: str
    ConstructionYear: float
    FloodingZone: str
    Kitchen: str
    PEB: str
    Province: str
    Region: str
    StateOfBuilding: str
    SubtypeOfProperty: str
    TypeOfSale: str
    BathroomCount: float
    BedroomCount: int
    Garden: float
    GardenArea: float
    LivingArea: float
    NumberOfFacades: int
    PostalCode: int
    RoomCount: int
    ShowerCount: int
    SurfaceOfPlot: float
    Terrace: float
    ToiletCount: float
    TypeOfProperty: int



@app.post("/predict")
def predict(features: Features):
    # Converting the features to a DataFrame
    feature_dict = features.dict()
    df = pd.DataFrame([feature_dict])

    # Predicting
    y_pred = loaded_model.predict(df)

    # Returning the predicted price
    predicted_price = round(np.exp(y_pred[0]), 1)
    return {"predicted_price": predicted_price}


# This method helps you understand how well the model is performing,
# by comparing the actual prices to the predicted prices on cleaned_data.csv (cleaned dataset).

@app.get("/evaluate")
def evaluate():
    df_pd = pd.read_csv("cleaned_data.csv")
    features = df_pd.drop(['Price'], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(features, np.log(df_pd['Price']), test_size=0.2, random_state=0)

    y_pred = loaded_model.predict(X_test)

    # Converting log prices back to original prices
    original_prices = np.exp(y_test)
    predicted_prices = np.exp(y_pred)

    # Creating a list of dictionaries with original and predicted prices
    results = [{"Real Price": round(orig,1), "Predicted Price": round(pred,1)} for orig, pred in
               zip(original_prices, predicted_prices)]

    return {"results": results}


# This method helps an user to download test data directly from web app
@app.get("/download_test_data")
def download_test_data():
    # Reading the cleaned data and splitting into train and test sets
    df_pd = pd.read_csv("cleaned_data.csv")
    features = df_pd.drop(['Price'], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(features, np.log(df_pd['Price']), test_size=0.2, random_state=0)

    # Saving X_test to a CSV file
    test_data_filename = "X_test.csv"
    X_test.to_csv(test_data_filename, index=False)

    # Returning the file as a response
    return FileResponse(path=test_data_filename, filename=test_data_filename, media_type='text/csv')


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

