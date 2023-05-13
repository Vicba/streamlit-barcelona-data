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
    st_folium(m)

    #########################################################################################################################################################
