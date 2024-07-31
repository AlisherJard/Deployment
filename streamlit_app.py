import streamlit as st
import requests
from PIL import Image

# Load images
header_image = Image.open("ezgif-3-63d9b88cbf.jpg")  # Replace with your own image path
predict_image = Image.open("360_F_332243559_TxD3apokkJJqdtXBmLIwvyXTL8hb1xQL.jpg")


st.title("Real Estate Price Predictor (Belgium) ")

st.image(header_image, use_column_width=True)

# Inputs for prediction
st.header("Input your values here:")
District = st.text_input("District", "Brugge")
ConstructionYear = st.number_input("Construction Year", 2026)
FloodingZone = st.number_input("Flooding Zone", 1)
Kitchen = st.number_input("Kitchen", 1)
Locality = st.text_input("Locality", "Some Locality")
PEB = st.text_input("PEB", "A")
Province = st.text_input("Province", "Some Province")
Region = st.text_input("Region", "Some Region")
StateOfBuilding = st.text_input("State Of Building", "New")
SubtypeOfProperty = st.text_input("Subtype Of Property", "House")
TypeOfSale = st.text_input("Type Of Sale", "Private")
BathroomCount = st.number_input("Bathroom Count", 2)
BedroomCount = st.number_input("Bedroom Count", 3)
Fireplace = st.number_input("Fireplace", 1)
Furnished = st.number_input("Furnished", 0)
Garden = st.number_input("Garden", 1)
GardenArea = st.number_input("Garden Area", 100.0)
LivingArea = st.number_input("Living Area", 150.0)
NumberOfFacades = st.number_input("Number Of Facades", 4)
PostalCode = st.number_input("Postal Code", 8000)
RoomCount = st.number_input("Room Count", 6)
ShowerCount = st.number_input("Shower Count", 2)
SurfaceOfPlot = st.number_input("Surface Of Plot", 200.0)
SwimmingPool = st.number_input("Swimming Pool", 0)
Terrace = st.number_input("Terrace", 1)
ToiletCount = st.number_input("Toilet Count", 2)
TypeOfProperty = st.selectbox("Type Of Property", ['1', '2'])

# Button to submit the form
if st.button("Predict Price"):
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
        "Fireplace": Fireplace,
        "Furnished": Furnished,
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
        label="Download X_test.csv",
        data=response.content,
        file_name="X_test.csv",
        mime="text/csv"
    )
else:
    st.write("Failed to fetch the test data. Please try again later.")