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
    st.write("This is a data set of Barcelona")


elif dataset == "Population":
    df = pd.read_csv("./data/population.csv")
    # delete page content

elif dataset == "Unemployment":
    df = pd.read_csv("./data/unemployment.csv")
elif dataset == "GDP":
    df = pd.read_csv("./data/gdp.csv")
elif dataset == "Tourism":
    df = pd.read_csv("./data/tourism.csv")
