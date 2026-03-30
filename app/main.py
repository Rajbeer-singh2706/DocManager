#  ALL Import Statements

import streamlit as st 
import os 

# BASE_DIR: E:\PROJECTS_DIR\DocManager
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print("BASE_DIR:", BASE_DIR)

### My own modules import 
from tabs import render_upload_tab, render_search_tab, render_analytics_tab
from db.database import DatabaseManager


########## Title #############
st.set_page_config(page_title="DocManager", layout="wide")
st.title("Smart PDF Document Manager")


### INitialize DB 
def init_db():
    db = DatabaseManager()
    db.close()

########### TABS ################
st.divider()

upload_tab, search_tab, analytics_tab = st.tabs(["Upload", "Search", "Analytics"])

with upload_tab:
    render_upload_tab()

with search_tab:
    render_search_tab()

with analytics_tab:
    render_analytics_tab()


st.divider()