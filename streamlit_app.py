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
ConstructionYear = st.selectbox("Construction Year", [1900.0, 1901.0, 1902.0, 1903.0, 1904.0, 1905.0, 1906.0, 1907.0,
                                                         1908.0, 1909.0, 1910.0, 1911.0, 1912.0, 1913.0, 1914.0, 1915.0,
                                                         1916.0, 1917.0, 1918.0, 1919.0, 1920.0, 1921.0, 1922.0, 1923.0,
                                                         1924.0, 1925.0, 1926.0, 1927.0, 1928.0, 1929.0, 1930.0, 1931.0,
                                                         1932.0, 1933.0, 1934.0, 1935.0, 1936.0, 1937.0, 1938.0, 1939.0,
                                                         1940.0, 1941.0, 1942.0, 1943.0, 1944.0, 1945.0, 1946.0, 1947.0,
                                                         1948.0, 1949.0, 1950.0, 1951.0, 1952.0, 1953.0, 1954.0, 1955.0,
                                                         1956.0, 1957.0, 1958.0, 1959.0, 1960.0, 1961.0, 1962.0, 1963.0,
                                                         1964.0, 1965.0, 1966.0, 1967.0, 1968.0, 1969.0, 1970.0, 1971.0,
                                                         1972.0, 1973.0, 1974.0, 1975.0, 1976.0, 1977.0, 1978.0, 1979.0,
                                                         1980.0, 1981.0, 1982.0, 1983.0, 1984.0, 1985.0, 1986.0, 1987.0,
                                                         1988.0, 1989.0, 1990.0, 1991.0, 1992.0, 1993.0, 1994.0, 1995.0,
                                                         1996.0, 1997.0, 1998.0, 1999.0, 2000.0, 2001.0, 2002.0, 2003.0,
                                                         2004.0, 2005.0, 2006.0, 2007.0, 2008.0, 2009.0, 2010.0, 2011.0,
                                                         2012.0, 2013.0, 2014.0, 2015.0, 2016.0, 2017.0, 2018.0, 2019.0,
                                                         2020.0, 2021.0, 2022.0, 2023.0, 2024.0, 2025.0, 2026.0, 2027.0, 2033.0]
)
FloodingZone = st.number_input("Flooding Zone", 1)
Kitchen = st.number_input("Kitchen", 1)
Locality = st.text_input("Locality", "Some Locality")
PEB = st.text_input("PEB", "A")
Province = st.text_input("Province", "Some Province")
Region = st.text_input("Region", "Some Region")
StateOfBuilding = st.text_input("State Of Building", "New")
SubtypeOfProperty = st.text_input("Subtype Of Property", "House")
TypeOfSale = st.text_input("Type Of Sale", "Private")
BathroomCount = st.number_input("Bathroom Count", min_value=0, max_value=4)
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
ToiletCount = st.number_input("Toilet Count", min_value=0, max_value=6)
TypeOfProperty = st.selectbox("Type Of Property", ['Apartment', 'House'])

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
        label="Download dataset in csv",
        data=response.content,
        file_name="X_test.csv",
        mime="text/csv"
    )
else:
    st.write("Failed to fetch the test data. Please try again later.")