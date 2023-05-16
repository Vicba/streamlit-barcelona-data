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
        "The most used transport in Barcelona is the underground metro.. It’s an extensive network of rapid transit electrified railway lines that run mostly underground in central Barcelona and into the city’s suburbs. The network is operated by two separate companies: Transports Metropolitans de Barcelona (TMB) and Ferrocarrils de la Generalitat de Catalunya (FGC). Some data: the network consists of 12 lines, numbered L1 to L12, covering 144.3 kilometres of route and 180 stations. Tram: Opened in 2004, this metropolitan transport network has a fleet of 41 trams, 29 kilometres of route and six lines."
    )

    st.write(
        "Railway (FGC): Railway company which operates several unconnected lines in Catalonia, Spain. The lines operated include metro and commuter lines in and around the city of Barcelona, tourist mountain railways, and rural railway lines. Technical data: 19 lines, covering 271 kilometres of route and 97 stations."
    )

    st.write(
        "RENFE is the state-owned railway company in Spain. RENFE operates both local and International trains. In Spain, it’s train network is made up of 15.000 km of rail.",
        " Airport train: RENFE R2 Nord Line links Terminal 2 with Barcelona city centre. R2 Nord Line covers the route between Maçanet-Massanes by Granollers and Barcelona Airport.",
    )

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

    st.write("Now that we saw the train and metro stations, lets see the bus stops.")

    st.subheader("Bus stops")

    st.write(
        "When taking a bus in Barcelona, it is important to be familiar with the bus routes and timetables to plan your journey. Make sure to have a valid ticket or travel card before boarding and remember to validate it once on the bus. Pay attention to bus stops and signs, waiting at the designated stop and checking the bus number and stop name. Barcelona's buses have priority measures, so be mindful of their right of way. Utilize real-time information through the TMB mobile app or digital displays at bus stops to stay updated on bus arrival times."
    )

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

    ############################################################################################################################################

    st.subheader("Lets see see the touristic places in Barcelona.")
    st.write("Click the sidebar on the left and select tourism to start exploring.")
