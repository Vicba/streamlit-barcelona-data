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

import warnings

warnings.filterwarnings("ignore")

import os


def app():
    st.title("Transportation")

    df = pd.read_csv("./data/transports.csv")

    st.subheader("Transportation metro")
    st.write(
        "These are the metro stations locations in Barcelona. Click one to see the name."
    )

    underground = df.loc[df["Transport"] == "Underground"]
    underground = underground[["Latitude", "Longitude", "Station"]]

    aboveground = df.loc[df["Transport"] != "Underground"]
    aboveground = aboveground[["Latitude", "Longitude", "Station"]]

    barcelona_coordinates = [41.3851, 2.1734]

    map_transport = folium.Map(
        location=barcelona_coordinates, tiles="OpenStreetMap", zoom_start=12
    )

    for each in underground.iterrows():
        folium.CircleMarker(
            [each[1]["Latitude"], each[1]["Longitude"]],
            radius=5,
            color="red",
            popup=each[1]["Station"],
            fill=True,
        ).add_to(map_transport)

    for each in aboveground.iterrows():
        folium.CircleMarker(
            [each[1]["Latitude"], each[1]["Longitude"]],
            radius=5,
            color="green",
            popup=each[1]["Station"],
            fill=True,
        ).add_to(map_transport)

    st.write("**Green = aboveground, Red = underground**")

    folium_static(map_transport)

    ############################################################################################################################################

    st.subheader("Bus stops")

    busstop_df = pd.read_csv("./data/bus_stops.csv")

    total_bus_stops = busstop_df.shape[0]

    # Filter the bus stop data to show only day bus stops
    daybus = busstop_df.loc[busstop_df["Transport"] == "Day bus stop"]

    # Create a folium map object
    map_busstop = folium.Map(
        location=barcelona_coordinates, tiles="OpenStreetMap", zoom_start=12
    )

    # Add a marker for each day bus stop
    for each in daybus[:100].iterrows():
        folium.Marker(
            [each[1]["Latitude"], each[1]["Longitude"]],
            popup=str(each[1]["Bus.Stop"]),
            icon=folium.Icon(color="red", icon="stop"),
        ).add_to(map_busstop)

    # Display the map in Streamlit
    st.subheader("Day Bus Stops in Barcelona")
    st.markdown(
        "**Note:** Only the first 100 day bus stops are shown. There are a total of **{}** day bus stops in Barcelona.".format(
            total_bus_stops
        )
    )
    folium_static(map_busstop)
