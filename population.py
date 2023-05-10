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

import warnings

warnings.filterwarnings("ignore")

import os


def app():
    df = pd.read_csv("./data/population.csv")

    # Title and subtitle
    st.title("Population")
    st.subheader("The Raw Data")

    st.write(df.head())

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
        "Over fice years there is no significant gender change in the population of the city"
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

    st.write("showing only year 2017 because it's almost the same for all years")

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
