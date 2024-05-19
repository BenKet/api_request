import streamlit as st
import pandas as pd
import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")
data = response.json()
for user in data['people']:
    print(user['name'])

print("People in Space: ", len(data['people']))


# Streamlit app
st.title('Number of people in space right now: ', len(data['people']))

st.write("Name of the poople in Space: ")
for user in data['people']:
    st.wirit(user['name'])
