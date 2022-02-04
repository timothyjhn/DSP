import streamlit as st
import sklearn as sk
import pandas as pd
import numpy as np
import pydeck as pdk
import altair as alt
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt



st.title("Smart Bridge Sustainment in the Circular Economy")

st.header("Gemeente Almere Bridge Data")
st.write("Welcome to our Webapp! In this web application we focus on bridges within the province of Flevoland as this province has the newest set of bridges. Below you will find metrics outlining the intial state of bridges in the province. In the future we intend to capture specific data from bridge stakeholders and assess the most effiecent place to recycle bridge parts.")

almere_data = pd.read_csv('Bridge_data.csv', encoding= 'unicode_escape')

st.text("Below is a complete list of bridges in Almere")
st.write(almere_data)


st.subheader("Construction Material Type with in the dataset")
st.write("Knowing the type of construction material used in the bridge is important for referbishment, from the data below we can see that concrete is the most abundant material to recycle bridge parts from, while Composet is the least.")
construction_type = (almere_data["ConstructionType"].value_counts())
st.bar_chart(construction_type)


st.subheader("Build Year of Bridge")
st.write("Build Year is also imporatnt in determining when a bridge should be prioritized for referbishment. As mentoned above, Flevoland bridges are relatively new, we can expect a large precentage of bridges will reach their Technical Life span around the year 2100. ")
build_year = (almere_data["Buildyear"].value_counts())
st.line_chart(build_year)


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
st.header("Overview of Maintainance State of Bridges")
st.write("With 61.8 precent of bridges in good condition, this is showing an overall good state of bridges in Flevoland. With time the state of each bridge will change with routine maintainance and may improve or indicate a need for repair.")
labels = 'Good', 'Reasonable', 'Moderate', 'Perfect', 'poor'
sizes = [338, 127, 42, 26, 14]
explode = (0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)

st.write("With the map below, you can see the general location of where each bridge is located. In the future we would like to find the shortest route to transfer bridge parts from the closest bridge")

#interactive map

import streamlit.components.v1 as components

st.header("Interactive map of bridges")
st.markdown('Click on the markers to reveal more details about the bridge')

HtmlFile = open("Bridge_map.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
components.html(source_code, height = 500, width = 800)


#input option

import streamlit.components.v1 as components

st.header("New bridge data input")
st.markdown('Below you will find a system designed to add new bridge data to the database')

st.number_input("Asset number:")
st.text_input("Asset type:")
st.radio("Asset type:", ["Fiets-Voetbrug", "Verkeersbrug", "Duikerbrug"])
st.radio("Construction type:", ["Composiet", "Concrete", "Steel"])
st.selectbox("Maintanance state:", ["Perfect", "Good", "Reasonable", "Moderate", "Poor", "Very poor"])
st.number_input("Buildyear:")
st.selectbox("Maintainer:", ["SB AIB", "Staatsbosbeheer", "Flevolandschap", "Provincie Flevoland"])
st.radio("Status:", ["Existing", "History", "Plan"])
st.number_input("Width:")
st.number_input("Length:")
st.text_input("Area:")
st.text_input("Location:")
st.number_input("Latitude:")
st.number_input("Longitude:")
st.number_input("Passage road-width:")
st.number_input("Passage road-height:")
st.number_input("Passage sail-width:")
st.number_input("Passage sail-height:")
st.number_input("Technical lifespan expectancy:")
st.selectbox("Connection type:", ["Groengebieden/Parken", "Buitengebied", "Hoofdwegen", "Woongebied", "Bedrijventerreinen"])
st.text_input("Neighborhood:")
st.selectbox("City:", ["Almere Stad", "Almere Haven", "Almere Poort", "Almere Buiten", "Almere Hout"])
st.button("Submit")