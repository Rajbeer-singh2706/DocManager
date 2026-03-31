import streamlit as st
import os
from dotenv import load_dotenv
from service.analytic_service import AnalyticService

DB_PATH = os.path.join("data","documents.db")
PDF_DIR = os.path.join("storage", "pdfs")
THUMBNAIL_DIR = os.path.join("storage", "thumbnails")

if "show_reset"  not in st.session_state:
    st.session_state.show_reset = False 

class AdminTab:
    def __init__(self):
        pass
    
    @staticmethod
    def render_admin_tab(ADMIN_PASSWORD):
        #st.header("⚙️ Admin Controls")

        ############### RESET Analytics ##############
        if st.button("🧹 Reset Analytics"):
            AnalyticService.reset_analytics()
            st.success("Analytics reset successfully")
            st.rerun()
        
        st.divider()
        ############### CLEAN DATABASE ##############
        if st.button("🗑️ Clean Database"):
            st.write("EXECUTED ")
            st.session_state.show_reset = True
        
        if st.session_state.get("show_reset", False):
           st.write("CLENA ")
           password_input = st.text_input("Enter Admin Password to Confirm", type="password")
           if st.button("Confirm Reset"):
               if password_input == ADMIN_PASSWORD:
                   import shutil 
                   ################ DELETE DB ###############
                   if os.path.exists(DB_PATH):
                       os.remove(DB_PATH)
                       st.success("Database reset successfully")
                   else:
                       st.warning("Database file not found.")
                
                   ################ DELETE UPLOADED FILES ###############
                   shutil.rmtree(PDF_DIR, ignore_errors=True)
                   shutil.rmtree(THUMBNAIL_DIR, ignore_errors=True)
                   #os.makedirs(PDF_DIR, exist_ok=True)
                   #os.makedirs(THUMBNAIL_DIR, exist_ok=True)

                   st.success("System reset successfully. Restart APP ")
                   st.session_state.show_reset = False
                   st.rerun()
               else:
                    st.error("Incorrect password. Reset aborted.")
                    st.session_state.show_reset = False 
                    st.rerun()


# When we click on button , then it reloads the application 
# thats why we need to set the variable 

