from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Loading of the trained model
loaded_model = joblib.load('model_rf.pkl')

app = FastAPI()

# Defining the Features class to match our dataset's structure
class Features(BaseModel):
    District: str
    ConstructionYear: float
    FloodingZone: int
    Kitchen: int
    Locality: str
    PEB: str
    Province: str
    Region: str
    StateOfBuilding: str
    SubtypeOfProperty: str
    TypeOfSale: str
    BathroomCount: int
    BedroomCount: int
    Fireplace: int
    Furnished: int
    Garden: int
    GardenArea: float
    LivingArea: float
    NumberOfFacades: int
    PostalCode: int
    RoomCount: int
    ShowerCount: int
    SurfaceOfPlot: float
    SwimmingPool: int
    Terrace: int
    ToiletCount: int
    TypeOfProperty: str


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
# by comparing the actual prices to the predicted prices on the test set.

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
    results = [{"original_price": round(orig,1), "predicted_price": round(pred,1)} for orig, pred in
               zip(original_prices, predicted_prices)]

    return {"results": results}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)