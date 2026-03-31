#  ALL Import Statements

import streamlit as st 
import os , sys 

# BASE_DIR: E:\PROJECTS_DIR\DocManager
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)
print("BASE_DIR:", BASE_DIR)

### My own modules import 

from db.database import DatabaseManager
from tabs.upload_tab import UploadTab
from tabs.search_tab import render_search_tab
from tabs.analytics_tab import AnalyticsTab

########## Title #############
st.set_page_config(page_title="DocManager", layout="wide")
st.title("Smart PDF Document Manager")

### INitialize DB ---> create Inital Setup ##########
db = DatabaseManager()
db.init_db()
db.close()

########### TABS ################
st.divider()

upload_tab, search_tab, analytics_tab = st.tabs(["Upload", "Search", "Analytics"])

with upload_tab:
    #render_upload_tab()
    upload_tab_instance = UploadTab(st)
    upload_tab_instance.render_upload_tab()

with search_tab:
    print("############################ LOADED SEARCH TAB ############################")
    #search_tab_instance = SearchTab(st)
    #search_tab_instance.render_search_tab()
    render_search_tab()

with analytics_tab:
    print("############################ LOADED ANALYTICS TAB ############################")
    # Initialize the analytics service
    analytics_tab = AnalyticsTab()
    analytics_tab.render_analytics_tab()


st.divider()