#  ALL Import Statements
import streamlit as st
from dotenv import load_dotenv
import os , sys 

# BASE_DIR: E:\PROJECTS_DIR\DocManager
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)
print("BASE_DIR:", BASE_DIR)

load_dotenv(os.path.join(BASE_DIR, ".env"))
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")


### My own modules import
from db.database import DatabaseManager
from tabs.upload_tab import UploadTab
from tabs.search_tab import render_search_tab
from tabs.analytics_tab import AnalyticsTab
from tabs.admin_tab import AdminTab

########## Title #############
st.set_page_config(page_title="DocManager", layout="wide")
st.title("Smart PDF Document Manager")

### Initialize DB ---> create Initial Setup ##########
db = DatabaseManager()
db.init_db()
db.close()

########### TABS ################
#st.divider()

upload_tab, search_tab, analytics_tab,admin_tab = st.tabs(["Upload", "Search", "Analytics", "⚙️ Admin Control"])

with upload_tab:
    print("############################ LOADED UPLOAD TAB ############################")
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

with admin_tab:
    print("########################## LOADED ADMIN TAB ####################")
    AdminTab.render_admin_tab(ADMIN_PASSWORD)

#st.divider()