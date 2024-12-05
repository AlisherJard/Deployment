import streamlit as st
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from PIL import Image

# Load the trained model
loaded_model = joblib.load('model_rf.pkl')

# Load header and prediction images
header_image = Image.open("header.jpg")
predict_image = Image.open("predict.jpg")

st.title("Real Estate Price Predictor (Belgium)")
st.image(header_image, use_column_width=True)

# Description
st.markdown("""
The overall dataset comprises 48,574 data points. The model was trained using 80% of these data points and tested on the remaining 20%.
You can evaluate the model’s accuracy by comparing predicted prices with actual prices.
""")

# Input Form
st.header("Input Property Details")
District = st.selectbox("District:",
                        ['Halle-Vilvoorde', 'Dinant', 'Huy', 'Aalst', 'Brugge', 'Eeklo', 'Mons', 'Oostend', 'Ath',
                         'Sint-Niklaas',
                         'Waremme', 'Hasselt', 'Gent', 'Tournai', 'Virton', 'Liège', 'Mouscron', 'Philippeville',
                         'Tielt', 'Nivelles',
                         'Bastogne', 'Maaseik', 'Namur', 'Leuven', 'Turnhout', 'Charleroi', 'Marche-en-Famenne',
                         'Thuin', 'Soignies',
                         'Mechelen', 'Brussels', 'Diksmuide', 'Veurne', 'Verviers', 'Antwerp', 'Tongeren',
                         'Dendermonde', 'Arlon',
                         'Neufchâteau', 'Ieper', 'Kortrijk', 'Oudenaarde', 'Roeselare'])

ConstructionYear = st.selectbox("Construction Year:", [int(year) for year in range(1900, 2034)])

FloodingZone = st.selectbox("Flooding Zone:",
                            ['False', 'POSSIBLE_N_CIRCUMSCRIBED_WATERSIDE_ZONE', 'RECOGNIZED_FLOOD_ZONE',
                             'RECOGNIZED_N_CIRCUMSCRIBED_FLOOD_ZONE', 'CIRCUMSCRIBED_WATERSIDE_ZONE',
                             'POSSIBLE_FLOOD_ZONE',
                             'NON_FLOOD_ZONE', 'POSSIBLE_N_CIRCUMSCRIBED_FLOOD_ZONE',
                             'RECOGNIZED_N_CIRCUMSCRIBED_WATERSIDE_FLOOD_ZONE',
                             'CIRCUMSCRIBED_FLOOD_ZONE'])

Kitchen = st.selectbox("Kitchen Type:",
                       ['USA_HYPER_EQUIPPED', 'INSTALLED', 'USA_SEMI_EQUIPPED', 'USA_UNINSTALLED', 'HYPER_EQUIPPED',
                        'False', 'USA_INSTALLED', 'SEMI_EQUIPPED', 'NOT_INSTALLED'])

PEB = st.selectbox("PEB (Energy Budget):", ['C', 'E', 'A_A+', 'A', 'A++', 'G', 'B', 'F', 'B_A', 'D', 'A+', 'False'])

Province = st.selectbox("Province:", ['West Flanders', 'Flemish Brabant', 'Luxembourg', 'Walloon Brabant', 'Brussels',
                                      'Antwerp', 'Hainaut', 'Namur', 'Liège', 'Limburg', 'East Flanders'])

Region = st.selectbox("Region:", ['Brussels', 'Wallonie', 'Flanders'])

StateOfBuilding = st.selectbox("Condition of the Building:", ['TO_RENOVATE', 'JUST_RENOVATED', 'False', 'TO_BE_DONE_UP',
                                                              'TO_RESTORE', 'GOOD', 'AS_NEW'])

SubtypeOfProperty = st.selectbox("Property Subtype:",
                                 ['apartment_block', 'country_cottage', 'mansion', 'penthouse', 'farmhouse',
                                  'other_property', 'kot', 'pavilion', 'triplex', 'service_flat',
                                  'flat_studio', 'apartment', 'ground_floor', 'duplex', 'mixed_use_building',
                                  'bungalow', 'manor_house', 'loft', 'villa', 'town_house', 'chalet', 'house',
                                  'exceptional_property'])

TypeOfSale = st.selectbox("Type of Sale:", ['annuity_lump_sum', 'annuity_monthly_amount', 'residential_monthly_rent',
                                            'residential_sale'])

BathroomCount = st.number_input("Bathrooms:", min_value=0, max_value=4)
BedroomCount = st.number_input("Bedrooms:", min_value=0, max_value=8)
Garden = st.selectbox("Is there a Garden?", [False, True])
GardenArea = st.number_input("Garden Area (m²):", min_value=0, max_value=92828)
LivingArea = st.number_input("Living Area (m²):", min_value=12, max_value=1000)
NumberOfFacades = st.selectbox("Number of Facades:", [0, 1, 2, 3, 4, 5, 6])
PostalCode = st.selectbox("Postal Code:", [int(code) for code in range(1000, 9992)])
RoomCount = st.selectbox("Number of Rooms:", range(0, 15))
ShowerCount = st.selectbox("Number of Showers:", range(0, 15))
SurfaceOfPlot = st.number_input("Plot Surface (m²):", min_value=0, max_value=4000)
Terrace = st.selectbox("Is there a Terrace?", [False, True])
ToiletCount = st.number_input("Toilets:", min_value=0, max_value=6)
TypeOfProperty = 1 if st.selectbox("Property Type:", ["House", "Apartment"]) == "House" else 2

# Button to predict price
if st.button("Predict Price"):
    input_features = {
        "District": District,
        "ConstructionYear": ConstructionYear,
        "FloodingZone": FloodingZone,
        "Kitchen": Kitchen,
        "PEB": PEB,
        "Province": Province,
        "Region": Region,
        "StateOfBuilding": StateOfBuilding,
        "SubtypeOfProperty": SubtypeOfProperty,
        "TypeOfSale": TypeOfSale,
        "BathroomCount": BathroomCount,
        "BedroomCount": BedroomCount,
        "Garden": Garden,
        "GardenArea": GardenArea,
        "LivingArea": LivingArea,
        "NumberOfFacades": NumberOfFacades,
        "PostalCode": PostalCode,
        "RoomCount": RoomCount,
        "ShowerCount": ShowerCount,
        "SurfaceOfPlot": SurfaceOfPlot,
        "Terrace": Terrace,
        "ToiletCount": ToiletCount,
        "TypeOfProperty": TypeOfProperty
    }

    df = pd.DataFrame([input_features])
    y_pred = loaded_model.predict(df)
    predicted_price = round(np.exp(y_pred[0]), 1)
    st.success(f"The predicted price is: {predicted_price} euros")
    st.image(predict_image, use_column_width=True)

# Evaluation
st.header("Evaluate Model")
if st.button("Evaluate"):
    df_pd = pd.read_csv("cleaned_data.csv")
    features = df_pd.drop(['Price'], axis=1)
    _, X_test, _, y_test = train_test_split(features, np.log(df_pd['Price']), test_size=0.2, random_state=0)

    y_pred = loaded_model.predict(X_test)
    results = pd.DataFrame({
        "Real Price": np.exp(y_test),
        "Predicted Price": np.exp(y_pred)
    })

    st.write(results.head(10))

    # Download Test Data
    st.download_button("Download Test Data", X_test.to_csv(index=False), "X_test.csv", "text/csv")
