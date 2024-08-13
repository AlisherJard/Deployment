import streamlit as st
import requests
from PIL import Image


header_image = Image.open("header.jpg")
predict_image = Image.open("predict.jpg")


st.title("Real Estate Price Predictor (Belgium)")
st.markdown('The overall dataset comprises 48,574 data points. The model was trained using 80% of these data points and tested on the remaining 20%. '
            'You can download the 20% test data, along with a comparison of the predicted prices and the actual prices, to evaluate the model’s accuracy.')

st.image(header_image, use_column_width=True)

# Inputs for prediction
st.header("Input your values here:")
District = st.selectbox("Which district is this?", ['Halle-Vilvoorde', 'Dinant', 'Huy', 'Aalst', 'Brugge', 'Eeklo', 'Mons',
                                      'Oostend', 'Ath', 'Sint-Niklaas', 'Waremme', 'Hasselt', 'Gent', 'Tournai',
                                      'Virton', 'Liège', 'Mouscron', 'Philippeville', 'Tielt', 'Nivelles', 'Bastogne',
                                      'Maaseik', 'Namur', 'Leuven', 'Turnhout', 'Charleroi', 'Marche-en-Famenne', 'Thuin',
                                      'Soignies', 'Mechelen', 'Brussels', 'Diksmuide', 'Veurne', 'Verviers', 'Antwerp',
                                      'Tongeren',  'Dendermonde', 'Arlon', 'Neufchâteau', 'Ieper', 'Kortrijk', 'Oudenaarde', 'Roeselare'])

ConstructionYear = st.selectbox("In what year was it constructed, or when is it expected to be completed?", [int(year) for year in range(1900, 2034)])

FloodingZone = st.selectbox("Is this area a flood zone?", ['False', 'POSSIBLE_N_CIRCUMSCRIBED_WATERSIDE_ZONE', 'RECOGNIZED_FLOOD_ZONE', 'RECOGNIZED_N_CIRCUMSCRIBED_FLOOD_ZONE',
                                                 'CIRCUMSCRIBED_WATERSIDE_ZONE', 'POSSIBLE_FLOOD_ZONE', 'NON_FLOOD_ZONE', 'POSSIBLE_N_CIRCUMSCRIBED_FLOOD_ZONE',
                                                 'RECOGNIZED_N_CIRCUMSCRIBED_WATERSIDE_FLOOD_ZONE', 'CIRCUMSCRIBED_FLOOD_ZONE'])

Kitchen = st.selectbox("What type of kitchen(s) is it?", ['USA_HYPER_EQUIPPED', 'INSTALLED', 'USA_SEMI_EQUIPPED', 'USA_UNINSTALLED', 'HYPER_EQUIPPED',
                                      'False', 'USA_INSTALLED', 'SEMI_EQUIPPED', 'NOT_INSTALLED'])


PEB = st.selectbox("What is your Personal Energy Budget (PEB)?", ['C', 'E', 'A_A+', 'A', 'A++', 'G', 'B', 'F', 'B_A', 'D', 'A+', 'False'])


Province = st.selectbox("Which province is this?", ['West Flanders', 'Flemish Brabant', 'Luxembourg', 'Walloon Brabant', 'Brussels',
                                      'Antwerp', 'Hainaut', 'Namur', 'Liège', 'Limburg', 'East Flanders'])

Region = st.selectbox("Which region is this?", ['Brussels', 'Wallonie', 'Flanders'])

StateOfBuilding = st.selectbox("What is the condition of the building?", ['TO_RENOVATE', 'JUST_RENOVATED', 'False', 'TO_BE_DONE_UP',
                                                      'TO_RESTORE', 'GOOD', 'AS_NEW'])

SubtypeOfProperty = st.selectbox("What is the property subtype?", ['apartment_block', 'country_cottage', 'mansion', 'penthouse',
                                                          'farmhouse', 'other_property', 'kot', 'pavilion', 'triplex',
                                                          'service_flat', 'flat_studio', 'apartment', 'ground_floor', 'duplex',
                                                          'mixed_use_building', 'bungalow', 'manor_house', 'loft', 'villa',
                                                          'town_house', 'chalet', 'house', 'exceptional_property'])

TypeOfSale = st.selectbox("What is the type of sale?", ['annuity_lump_sum', 'annuity_monthly_amount', 'residential_monthly_rent', 'residential_sale'])

BathroomCount = st.number_input("How many bathrooms are there?", min_value=0, max_value=4)

BedroomCount = st.number_input("How many bedrooms are there?", min_value=0, max_value=8)


# The overall dataset consists of 48,574 data points. The model was trained on 80% of these data points and
# tested on the remaining 20%.

Garden = st.selectbox("Is there a garden?", [False, True])

GardenArea = st.number_input("What is the size of a garden in square meters (m²)?", min_value=0, max_value=92828)

LivingArea = st.number_input("What is the size of a living area in square meters (m²)?", min_value=12, max_value=1000)

NumberOfFacades = st.selectbox("How many facades does the building have?", [0, 1, 2, 3, 4, 5, 6])

PostalCode = st.selectbox("What is the postal code?", [int(code) for code in range(1000, 9992)])

RoomCount = st.selectbox("How many rooms are there?", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

ShowerCount = st.selectbox("How many showers are there?", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14])

SurfaceOfPlot = st.number_input("What is the size of a surface of plot in square meters (m²)?", min_value=0, max_value=4000)

Terrace = st.selectbox("Does it have a terrace?", [False, True])

ToiletCount = st.number_input("How many toilets are there?", min_value=0, max_value=6)

# TypeOfProperty = st.selectbox("Is it a 1) House or 2) Apartment?", [1, 2])

TypeOfProperty = st.selectbox("Select the type of property:", ["House", "Apartment"])

TypeOfProperty = 1 if TypeOfProperty == "House" else 2

# Button to submit the form
if st.button("Predict Price"):
    st.balloons()
    # Create a dictionary with the input features
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

    # Sending the request to the FastAPI prediction endpoint (connection to FastAPI back-end)
    response = requests.post("https://deployment-nlge.onrender.com/predict", json=input_features)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Based on the information you have provided, the price will be: {result['predicted_price']:.2f} euros")
        st.image(predict_image, use_column_width=True)
    else:
        st.error("An error occurred while making the prediction.")

# Evaluation of the model based on 9715 properties

st.header("Compare the actual prices with the predicted prices using the test data:")
if st.button("Evaluate"):
    # Sending the request to the FastAPI evaluate endpoint (connection to FastAPI back-end)
    response = requests.get("https://deployment-nlge.onrender.com/evaluate")
    if response.status_code == 200:
        results = response.json()["results"]
        st.write(results)
    else:
        st.error("An error occurred while evaluating the model.")


url = "https://deployment-nlge.onrender.com/download_test_data"

st.title("Download Test Data")

st.write("Click the button below to download the test data as a CSV file.")


# Fetch the data from the FastAPI endpoint
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Create a download button in Streamlit
    st.download_button(
        label="Download dataset in csv",
        data=response.content,
        file_name="X_test.csv",
        mime="text/csv"
    )
else:
    st.write("Failed to fetch the test data. Please try again later.")