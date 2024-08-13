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
District = st.selectbox("District", ['Halle-Vilvoorde', 'Dinant', 'Huy', 'Aalst', 'Brugge', 'Eeklo', 'Mons',
                                      'Oostend', 'Ath', 'Sint-Niklaas', 'Waremme', 'Hasselt', 'Gent', 'Tournai',
                                      'Virton', 'Liège', 'Mouscron', 'Philippeville', 'Tielt', 'Nivelles', 'Bastogne',
                                      'Maaseik', 'Namur', 'Leuven', 'Turnhout', 'Charleroi', 'Marche-en-Famenne', 'Thuin',
                                      'Soignies', 'Mechelen', 'Brussels', 'Diksmuide', 'Veurne', 'Verviers', 'Antwerp',
                                      'Tongeren',  'Dendermonde', 'Arlon', 'Neufchâteau', 'Ieper', 'Kortrijk', 'Oudenaarde', 'Roeselare'])

ConstructionYear = st.selectbox("Construction Year", [int(year) for year in range(1900, 2034)])

FloodingZone = st.selectbox("Flooding Zone", ['False', 'POSSIBLE_N_CIRCUMSCRIBED_WATERSIDE_ZONE', 'RECOGNIZED_FLOOD_ZONE', 'RECOGNIZED_N_CIRCUMSCRIBED_FLOOD_ZONE',
                                                 'CIRCUMSCRIBED_WATERSIDE_ZONE', 'POSSIBLE_FLOOD_ZONE', 'NON_FLOOD_ZONE', 'POSSIBLE_N_CIRCUMSCRIBED_FLOOD_ZONE',
                                                 'RECOGNIZED_N_CIRCUMSCRIBED_WATERSIDE_FLOOD_ZONE', 'CIRCUMSCRIBED_FLOOD_ZONE'])

Kitchen = st.selectbox("Kitchen", ['USA_HYPER_EQUIPPED', 'INSTALLED', 'USA_SEMI_EQUIPPED', 'USA_UNINSTALLED', 'HYPER_EQUIPPED',
                                      'False', 'USA_INSTALLED', 'SEMI_EQUIPPED', 'NOT_INSTALLED'])


PEB = st.selectbox("PEB", ['C', 'E', 'A_A+', 'A', 'A++', 'G', 'B', 'F', 'B_A', 'D', 'A+', 'False'])


Province = st.selectbox("Province", ['West Flanders', 'Flemish Brabant', 'Luxembourg', 'Walloon Brabant', 'Brussels',
                                      'Antwerp', 'Hainaut', 'Namur', 'Liège', 'Limburg', 'East Flanders'])

Region = st.selectbox("Region", ['Brussels', 'Wallonie', 'Flanders'])

StateOfBuilding = st.selectbox("State Of Building", ['TO_RENOVATE', 'JUST_RENOVATED', 'False', 'TO_BE_DONE_UP',
                                                      'TO_RESTORE', 'GOOD', 'AS_NEW'])

SubtypeOfProperty = st.selectbox("Subtype Of Property", ['apartment_block', 'country_cottage', 'mansion', 'penthouse',
                                                          'farmhouse', 'other_property', 'kot', 'pavilion', 'triplex',
                                                          'service_flat', 'flat_studio', 'apartment', 'ground_floor', 'duplex',
                                                          'mixed_use_building', 'bungalow', 'manor_house', 'loft', 'villa',
                                                          'town_house', 'chalet', 'house', 'exceptional_property'])

TypeOfSale = st.selectbox("Type Of Sale", ['annuity_lump_sum', 'annuity_monthly_amount', 'residential_monthly_rent', 'residential_sale'])

BathroomCount = st.number_input("Bathroom Count", min_value=0, max_value=4)

BedroomCount = st.number_input("Bedroom Count", min_value=0, max_value=8)


# The overall dataset consists of 48,574 data points. The model was trained on 80% of these data points and
# tested on the remaining 20%.

Garden = st.selectbox("Do you have a garden?", [False, True])

GardenArea = st.number_input("Garden Area (m²)", min_value=0, max_value=92828)

LivingArea = st.number_input("Living Area (m²)", min_value=12, max_value=1000)

NumberOfFacades = st.selectbox("How many facades?", [0, 1, 2, 3, 4, 5, 6])

PostalCode = st.selectbox("Postal Code", [int(code) for code in range(1000, 9992)])

RoomCount = st.selectbox("How many rooms?", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

ShowerCount = st.selectbox("How many showers?", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14])

SurfaceOfPlot = st.number_input("Surface Of Plot (m²)", min_value=0, max_value=4000)

Terrace = st.selectbox("Is there a terrace?", [0, 1])

ToiletCount = st.number_input("How many toilets?", min_value=0, max_value=6)

TypeOfProperty = st.selectbox("Is it 1) House, 2) Apartment ?", [1, 2])

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

st.header("Evaluate the Predictor based on Test Data (9715 properties):")
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