import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

import plotly
from plotly.offline import init_notebook_mode, iplot
import plotly.express as px

init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.offline as offline

offline.init_notebook_mode()
from plotly import tools
import plotly.tools as tls

import folium
from folium import plugins
from folium.plugins import HeatMap

from streamlit_folium import folium_static
import streamlit_folium
from streamlit_folium import st_folium


import warnings

warnings.filterwarnings("ignore")


import os
import csv
import requests


def app():
    st.title("Tourism")

    st.write(
        "Barcelona is one of the most visited cities in Europe. In 2019, the city received 9.5 million tourists, and in 2018, the city received 8.7 million tourists. The city is also the 4th most visited city in Europe, after London, Paris, and Rome. Tourism in Barcelona is strongly influenced by international visitors. In 2019, 86% of tourists were international visitors, while 14% were domestic visitors. The city is also the 12th most visited city in the world, after Bangkok, London, Paris, Dubai, Singapore, Kuala Lumpur, New York City, Istanbul, Tokyo, Antalya, and Mumbai."
    )

    st.write("Lets see some hotels in Barcelona that accomodate these tourists.")

    st.subheader("Hotels")

    # Load data from JSON file
    url = "./data/hotels.json"
    data = pd.read_json(url)

    print(data.columns)
    # Select relevant columns
    # Select relevant columns and extract x and y coordinates
    data = data[["name", "geo_epgs_4326"]]
    data["geo_epgs_4326_x"] = data["geo_epgs_4326"].apply(lambda x: x["x"])
    data["geo_epgs_4326_y"] = data["geo_epgs_4326"].apply(lambda x: x["y"])

    # Create map object
    m = folium.Map(location=[41.3887901, 2.1589899], zoom_start=12)

    # Add markers for each hotel
    for index, row in data.iterrows():
        name = row["name"]
        lat = row["geo_epgs_4326_x"]
        lon = row["geo_epgs_4326_y"]
        marker = folium.Marker(location=[lat, lon], tooltip=name)
        marker.add_to(m)

    # Display map in Streamlit app
    st.write("List and location of hotels in the city of Barcelona")

    st.write("Click the marker to see the name of the hotel.")

    st_folium(m)

    #########################################################################################################################################################

    st.subheader("Want to go out for a drink?")

    st.write(
        "List of music and drinks venues in the city of Barcelona that includes bars and pubs, cocktails, discotheques, karaokes, nightclubs, ballrooms, flamenco tablaos..."
    )

    # Load data from JSON file
    url = "https://www.bcn.cat/tercerlloc/files/cultura/opendatabcn_cultura_espais-de-musica-i-copes-js.json"
    data = pd.read_json(url)

    # Select relevant columns and rename
    data = data[["name", "geo_epgs_4326"]]
    data = data.rename(columns={"geo_epgs_4326": "coordinates"})

    # Extract latitude and longitude from coordinates
    data["latitude"] = data["coordinates"].apply(lambda x: x["x"])
    data["longitude"] = data["coordinates"].apply(lambda x: x["y"])

    # Create map object
    m = folium.Map(location=[41.3888, 2.159], zoom_start=13)

    # Add markers for each hotel
    for index, row in data.iterrows():
        name = row["name"]
        lat = row["latitude"]
        lon = row["longitude"]
        tooltip = f"{name}\n{name}"
        marker = folium.Marker(location=[lat, lon], tooltip=tooltip)
        marker.add_to(m)

    # Display map in Streamlit app
    folium_static(m)

    #########################################################################################################################################################

    st.subheader("Explore the Catalan culture!")

    st.write("Detail of main cultural interest points in the city of Barcelona.")

    st.write("Click the marker to see the name of the cultural interest point.")

    # Load data from JSON file
    url = "https://www.bcn.cat/tercerlloc/files/opendatabcn_pics-js.json"
    data = pd.read_json(url)

    # Select relevant columns and rename
    data = data[["name", "geo_epgs_4326"]]
    data = data.rename(columns={"geo_epgs_4326": "coordinates"})

    # Extract latitude and longitude from coordinates
    data["latitude"] = data["coordinates"].apply(lambda x: x["x"])
    data["longitude"] = data["coordinates"].apply(lambda x: x["y"])

    # Create map object
    m = folium.Map(location=[41.3888, 2.159], zoom_start=13)

    # Add markers for each hotel
    for index, row in data.iterrows():
        name = row["name"]
        lat = row["latitude"]
        lon = row["longitude"]
        tooltip = f"{name}\n{name}"
        marker = folium.Marker(location=[lat, lon], tooltip=tooltip)
        marker.add_to(m)

    # Display map in Streamlit app
    folium_static(m)

    #########################################################################################################################################################

    st.subheader("Want to see the beautiful views?")

    st.write(
        "Barcelona has some mountains that are worth visiting! Lets explore their locations to see the incredible views!"
    )

    st.write("List and location of viewpoints in the city of Barcelona.")

    # Load data from JSON file
    url = "https://www.bcn.cat/tercerlloc/files/opendatabcn_pics-js.json"
    data = pd.read_json(url)

    # Select relevant columns and rename
    data = data[["name", "geo_epgs_4326"]]
    data = data.rename(columns={"geo_epgs_4326": "coordinates"})

    # Extract latitude and longitude from coordinates
    data["latitude"] = data["coordinates"].apply(lambda x: x["x"])
    data["longitude"] = data["coordinates"].apply(lambda x: x["y"])

    # Create map object
    m = folium.Map(location=[41.3888, 2.159], zoom_start=13)

    # Add markers for each hotel
    for index, row in data.iterrows():
        name = row["name"]
        lat = row["latitude"]
        lon = row["longitude"]
        tooltip = f"{name}\n{name}"
        marker = folium.Marker(location=[lat, lon], tooltip=tooltip)
        marker.add_to(m)

    # Display map in Streamlit app
    folium_static(m)

    #########################################################################################################################################################

    st.subheader(
        "Thats it! Hope you enjoyed it and found it interesting! Lets travel to Barcelona!"
    )

    st.write(
        "Need to find more information about the city of Barcelona? Here are the locations of some tourist information offices. [clicke here!](https://www.barcelonaturisme.com/wv3/en/)"
    )
