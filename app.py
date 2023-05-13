import streamlit as st


class MultiPage:
    def __init__(self):
        self.pages = []
        self.page_titles = []

    def add_page(self, title, func):
        self.pages.append(func)
        self.page_titles.append(title)

    def show_page(self, title):
        idx = self.page_titles.index(title)
        self.pages[idx]()


# import your pages here
import home
import population
import transport
import tourism

# create an instance of the MultiPage class
app = MultiPage()


# add the home page to the app
app.add_page("Home", home.app)
app.add_page("Population", population.app)
app.add_page("Transport", transport.app)
app.add_page("Tourism", tourism.app)


# sidebar dropdown with dataset options
st.sidebar.header("Barcelona Data Sets")
dataset = st.sidebar.selectbox(
    "Select Dataset", ("Home", "Population", "Transport", "Tourism")
)

# show the appropriate page based on the user's selection
if dataset == "Home":
    home.app()
elif dataset == "Population":
    population.app()
elif dataset == "Transport":
    transport.app()
elif dataset == "Tourism":
    tourism.app()
