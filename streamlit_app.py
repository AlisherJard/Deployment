import streamlit as st
import requests
from PIL import Image


header_image = Image.open("header.jpg")
predict_image = Image.open("predict.jpg")


st.title("Real Estate Price Predictor (Belgium)")

st.image(header_image, use_column_width=True)

# Inputs for prediction
st.header("Input your values here:")
District = st.selectbox("District", ['Halle-Vilvoorde', 'Dinant', 'Huy', 'Aalst', 'Brugge', 'Eeklo', 'Mons',
                                      'Oostend', 'Ath', 'Sint-Niklaas', 'Waremme', 'Hasselt', 'Gent', 'Tournai',
                                      'Virton', 'Liège', 'Mouscron', 'Philippeville', 'Tielt', 'Nivelles', 'Bastogne',
                                      'Maaseik', 'Namur', 'Leuven', 'Turnhout', 'Charleroi', 'Marche-en-Famenne', 'Thuin',
                                      'Soignies', 'Mechelen', 'Brussels', 'Diksmuide', 'Veurne', 'Verviers', 'Antwerp',
                                      'Tongeren',  'Dendermonde', 'Arlon', 'Neufchâteau', 'Ieper', 'Kortrijk', 'Oudenaarde', 'Roeselare'])

ConstructionYear = st.selectbox("Construction Year", [float(year) for year in range(1900, 2034)])

FloodingZone = st.selectbox("Flooding Zone", ['False', 'POSSIBLE_N_CIRCUMSCRIBED_WATERSIDE_ZONE', 'RECOGNIZED_FLOOD_ZONE', 'RECOGNIZED_N_CIRCUMSCRIBED_FLOOD_ZONE',
                                                 'CIRCUMSCRIBED_WATERSIDE_ZONE', 'POSSIBLE_FLOOD_ZONE', 'NON_FLOOD_ZONE', 'POSSIBLE_N_CIRCUMSCRIBED_FLOOD_ZONE',
                                                 'RECOGNIZED_N_CIRCUMSCRIBED_WATERSIDE_FLOOD_ZONE', 'CIRCUMSCRIBED_FLOOD_ZONE'])

Kitchen = st.selectbox("Kitchen", ['USA_HYPER_EQUIPPED', 'INSTALLED', 'USA_SEMI_EQUIPPED', 'USA_UNINSTALLED', 'HYPER_EQUIPPED',
                                      'False', 'USA_INSTALLED', 'SEMI_EQUIPPED', 'NOT_INSTALLED'])

Locality = st.text_input("Locality", "Enter")

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

Garden = st.selectbox("Garden", [0.0, 1.0])

GardenArea = st.number_input("Garden Area", min_value=0.0, max_value=92828.0)

LivingArea = st.number_input("Living Area", min_value=12.0, max_value=1000.0)

NumberOfFacades = st.selectbox("Number Of Facades", [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0])

PostalCode = st.selectbox("Postal Code", [int(code) for code in range(0000, 9999)])

RoomCount = st.selectbox("Room Count", [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0])

ShowerCount = st.number_input("Shower Count", 2)

SurfaceOfPlot = st.number_input("Surface Of Plot", 200.0)

SwimmingPool = st.number_input("Swimming Pool", 0)

Terrace = st.number_input("Terrace", 1)

ToiletCount = st.number_input("Toilet Count", min_value=0, max_value=6)

TypeOfProperty = st.selectbox("Type Of Property (1 = House),(2 = Apartment)", [1, 2])

# Button to submit the form
if st.button("Predict Price"):
    st.balloons()
    # Create a dictionary with the input features
    input_features = {
        "District": District,
        "ConstructionYear": ConstructionYear,
        "FloodingZone": FloodingZone,
        "Kitchen": Kitchen,
        "Locality": Locality,
        "PEB": PEB,
        "Province": Province,
        "Region": Region,
        "StateOfBuilding": StateOfBuilding,
        "SubtypeOfProperty": SubtypeOfProperty,
        "TypeOfSale": TypeOfSale,
        "BathroomCount": BathroomCount,
        "BedroomCount": BedroomCount,
        "Fireplace": 0.0,
        "Furnished": 0.0,
        "Garden": Garden,
        "GardenArea": GardenArea,
        "LivingArea": LivingArea,
        "NumberOfFacades": NumberOfFacades,
        "PostalCode": PostalCode,
        "RoomCount": RoomCount,
        "ShowerCount": ShowerCount,
        "SurfaceOfPlot": SurfaceOfPlot,
        "SwimmingPool": SwimmingPool,
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