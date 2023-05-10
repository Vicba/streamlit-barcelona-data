import pandas as pd
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# make sidebar
st.sidebar.header("Barcelona Data Sets")

# sidebar drowndown with dataset options
dataset = st.sidebar.selectbox(
    "Select Dataset", ("Home", "Population", "Unemployment", "GDP", "Tourism")
)

# make a dataframe for each dataset
if dataset == "Home":
    # make header with picture
    st.image("./data/barcelona.jpg", width=700)
    st.title("Barcelona Data Sets")

    # subtitle
    st.subheader("Introduction")
    # intro text
    st.write(
        "Welcome to the Barcelona app, where you can explore and visualize various datasets related to the beautiful city of Barcelona. Whether you're a tourist planning a trip, a local resident interested in the city's demographics, or a data enthusiast, our app has something for you. Our dataset includes information on the city's neighborhoods, demographics, accommodations, and transportation. You can use our interactive visualizations to discover interesting trends and insights about Barcelona, such as the most popular neighborhoods for tourists or the average price of accommodations in different areas of the city. With the Barcelona app, you can plan your trip, learn more about the city, or satisfy your curiosity about its data."
    )


elif dataset == "Population":
    df = pd.read_csv("./data/population.csv")
    # delete page content


elif dataset == "Unemployment":
    df = pd.read_csv("./data/unemployment.csv")


elif dataset == "GDP":
    df = pd.read_csv("./data/gdp.csv")


elif dataset == "Tourism":
    df = pd.read_csv("./data/tourism.csv")
