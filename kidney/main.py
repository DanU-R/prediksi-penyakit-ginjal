#import library
import streamlit as st
from web_functions import load_data

from Tabs import home, predict, visualise

Tabs = {
	"home" : home,
	"prediction" : predict,
	"visualisation" : visualise
}

# membuat sidebar
st.sidebar.title("Navigasi")

#membuat radio option
page = st.sidebar.radio("Pages", list(Tabs.keys()))

#load_data
df, x, y = load_data()

#kondisi call app function
if page in ["prediction", "visualisation"]:
	Tabs[page].app(df, x,y)
else:
	Tabs[page].app()