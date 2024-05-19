import streamlit as st
import pandas as pd
import requests
import numpy as np
import json

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()

title_str = "Number of people in space right now: " + str(len(data['people']))

# Streamlit app
st.title(title_str)

names_of_people = "Name of the poople in Space: "

for user in data['people']:
    names_of_people += str(user['name']) + ", "

st.write(names_of_people)

response_iss = requests.get("http://api.open-notify.org/iss-now.json")
latitude = response_iss.json()['iss_position']['latitude']
longitude = response_iss.json()['iss_position']['longitude']

#Creat dataframe with the columns lat and lon and use the values of latitude and longitude as the values of the columns
#df = pd.DataFrame({'lat': latitude, 'lon': longitude})

df = pd.DataFrame(
    {'lat': [float(latitude)], 'lon': [float(longitude)]}
)

st.map(df)

