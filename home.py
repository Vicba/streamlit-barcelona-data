import streamlit as st

st.header("Home")


def app():
    st.image("./data/barcelona.jpg", width=700)
    st.title("Barcelona Data Sets")

    # subtitle
    st.subheader("Introduction")
    # intro text
    st.write(
        "Welcome to the Barcelona app, where you can explore various datasets related to the beautiful city of Barcelona. Whether you're a tourist planning a trip, a local resident interested in the city's demographics, or a data enthusiast. You can use the interactive visualizations to discover interesting trends and insights about Barcelona, such as the population, transport and tourism."
    )

    st.subheader("About the Data")
    st.write("The data used in this app was collected from the following sources:")
    st.write(
        "Kaggle: [Barcelona data sets](https://www.kaggle.com/datasets/xvivancos/barcelona-data-sets) and the website of [Open Data BCN](https://opendata-ajuntament.barcelona.cat/en) from the Barcelona City Council. "
    )

    st.subheader("Lets start exploring!")
    st.write("Let's guide you through the visualizations.")
    st.write(
        "Click on the sidebar on the left and select population to start exploring."
    )
