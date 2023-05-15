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

import json
from urllib.request import urlopen


import warnings

warnings.filterwarnings("ignore")

import os


def app():
    df = pd.read_csv("./data/population.csv")

    # Title and subtitle
    st.title("Population")
    st.subheader("The Raw Data")

    st.write("The raw data looks like this:")
    st.write(df.head())

    ###################################################################################################################################

    st.write(
        "so now we have an idea of what we’re working with, dataset of Barcelona population in 2013-2017 years by district, neighbourhood, gender and age."
    )

    st.write("Lets see the population of Barcelona year over year.")

    st.subheader("Population over the years")

    yearPOPULATION_count = df.groupby("Year")["Number"].sum().reset_index()

    fig = px.line(
        yearPOPULATION_count,
        x="Year",
        y="Number",
        title="Population Change From 2013 To 2017",
    )
    st.plotly_chart(fig)

    st.write(
        "In 2014 the population decreased a little, but in next few years comeback and eventually increased by 2.5% in 2017.",
        "With a total population of 1,620,809 in 2017, Barcelona is the second most populous city in Spain, behind Madrid, and the tenth-most populous municipality in the European Union.",
    )

    st.write("Lets see the population by age.")

    ###################################################################################################################################

    st.subheader("Gender distribution")
    # Calculate the male and female populations for each year
    male = df.loc[df["Gender"] == "Male"].groupby(["Year"])["Number"].sum()
    female = df.loc[df["Gender"] == "Female"].groupby(["Year"])["Number"].sum()

    # Create the bar chart using Plotly
    trace0 = go.Bar(
        x=male.index,
        y=male.values,
        name="Male",
        marker=dict(color="rgb(236,154,41)"),
        opacity=0.8,
    )

    trace1 = go.Bar(
        x=female.index,
        y=female.values,
        name="Female",
        marker=dict(color="rgb(168,32,26)"),
        opacity=0.8,
    )

    data = [trace0, trace1]
    layout = go.Layout(
        barmode="group",
        xaxis=dict(tickangle=-30),
        title="Gender-Wise Distribution Across the Years",
    )
    fig = go.Figure(data=data, layout=layout)

    # Display the chart in the Streamlit app
    st.plotly_chart(fig)

    st.write(
        "Over five years there is no significant gender change in the population of the city. We can see that there are a little more female inhabitants then male."
    )

    ###################################################################################################################################

    st.subheader("Population by District")

    # Filter the data for the selected year
    dist_df = df.loc[df["Year"] == 2017].groupby(["District.Name"])["Number"].sum()

    # Create the plot
    fig = px.bar(
        dist_df,
        x=dist_df.index,
        y=dist_df.values,
        color=dist_df.values,
        color_continuous_scale="Reds",
    )
    fig.update_layout(
        xaxis=dict(tickangle=-30),
        title="District-Wise Distribution of population (Year {})".format(2017),
    )

    # Show the plot
    st.plotly_chart(fig)

    st.write("You see only year 2017 because it's almost the same for all years")

    st.write(
        "In the barchart above we can see that the most populated district is Eixample, followed by Sant Martí and Sants-Montjuïc."
    )

    st.write("Lets see the immigration by nationality in Barcelona.")

    ###################################################################################################################################

    st.subheader("Immigrants by Nationality")
    # filter data for year 2017 and top 10 nationalities
    immig_df = pd.read_csv("./data/immigrants_by_nationality.csv")
    im_df = (
        immig_df.loc[immig_df["Year"] == 2017]
        .groupby(["Nationality"])["Number"]
        .sum()
        .sort_values(ascending=False)[:10]
    )

    trace0 = go.Bar(
        x=im_df.index,
        y=im_df.values,
        marker=dict(color=list(im_df.values), colorscale="Portland"),
    )

    data = [trace0]
    layout = go.Layout(
        xaxis=dict(tickangle=-30),
        title="Immigration By Nationality (Year 2017, Top 10)",
    )

    fig = go.Figure(data=data, layout=layout)

    st.plotly_chart(fig)

    st.write(
        "Most immigrants in Barcelona are actually from Spain. This could suggest that many people from other regions of Spain are moving to Barcelona, possibly due to employment opportunities, a desire for a change of scenery, or other factors."
    )

    ###################################################################################################################################

    st.write(
        "Now that we have seen the population by district, lets see the population by neighbourhood."
    )

    st.subheader("Population by neighbourhood")

    # Load the geojson data
    with urlopen(
        "https://raw.githubusercontent.com/martgnz/bcn-geodata/master/barris/barris.geojson"
    ) as response:
        gjson_neigh = json.load(response)

    # Rename the district to avoid errors with geojson
    gjson_neigh["features"][7]["properties"]["NOM"] = "el Poble Sec"

    # Load the population data
    data_population = pd.read_csv("./data/population.csv")

    data_2017 = data_population[data_population["Year"] == 2017]

    # Create choropleth map
    fig = px.choropleth_mapbox(
        data_population.groupby(["Neighborhood.Name"]).sum().reset_index(),
        geojson=gjson_neigh,
        color="Number",
        locations="Neighborhood.Name",
        featureidkey="properties.NOM",
        color_continuous_scale="YlOrRd",
        center={"lat": 41.395, "lon": 2.18},
        mapbox_style="open-street-map",
        zoom=11,
        opacity=0.9,
        height=620,
    )

    fig.update_layout(title="Population of Barcelona Neighborhoods in 2017")

    # Show the map using the plotly_chart function
    st.plotly_chart(fig)
    st.write(
        "Hover over the chart to see the neighbourhood name and the population amount."
    )

    ###################################################################################################################################µµ

    st.write("Now lets see the population pyramid.")

    df_2017 = df[df["Year"] == 2017]

    fig = px.funnel(
        df_2017,
        x="Number",
        y="Age",
        color="Gender",
        color_discrete_sequence=["rgb(225,70,84)", "rgb(30,40,100)"],
        height=600,
    )

    fig.update_layout(title="Population Pyramid", xaxis_title="Number")

    st.plotly_chart(fig)

    st.write(
        "We can clearly see that most of the people are between 30 and 60 years old. This is a regular chart for European countries."
    )

    st.subheader("Lets continue with the transport data.")
    st.write("Interested in taking the bus, metro or train in Barcelona?")
    st.write("Click the sidebar and select Transport.")
