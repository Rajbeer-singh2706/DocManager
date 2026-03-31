"""Analytics Tab - View document statistics and insights."""

import streamlit as st

from service.analytic_service import AnalyticService
from service.document_service import DocumentService

class AnalyticsTab:
    def __init__(self):
        self.analytics_service = AnalyticService() 
        self.document_service = DocumentService() 

    def render_analytics_tab(self):
        """Render the analytics tab interface."""
        st.write("Analytics")

        ############ 1. APP USAGE ########################
        st.subheader("APP Usage")
        app_data = self.analytics_service.get_app_visits()

        import pandas as pd 
        df = pd.DataFrame(app_data, columns=["Event Type", "Count"])
        st.dataframe(df)

        if df.empty:
            st.info("No analytics data available yet. Start using the app to see insights here!")
        else:
            st.bar_chart(df.set_index("Event Type"))
        
        st.divider()

        ############ 2. DOCUMENT INSIGHTS ########################
        #st.subheader("Document Insights")
        st.subheader("Document Progress")

        docs = self.document_service.get_all_documents()
        data = [] 
        for doc in docs:
            #unique_pages = self.analytics_service.get_unique_pages_viewed(doc.id) 
            unique_pages = AnalyticService().get_unique_pages_viewed(doc.id) 
            progress = (unique_pages / doc.total_pages) * 100 if doc.total_pages > 0 else 0

            data.append(
                    {
                        "Document": doc.name, 
                        "Pages Read": unique_pages,
                        "total Pages": doc.total_pages,
                        "Progress (%)": round(progress, 2)
                    }
            )
        
        df_docs = pd.DataFrame(data, columns=["Document", "Pages Read", "total Pages", "Progress (%)"])
        st.dataframe(df_docs)

        ##### END 


# def render_analytics_tab():
#     """Render the analytics tab interface."""
#     st.write("View your document analytics and statistics")

#     # Key metrics
#     st.subheader("Statistics")
#     col1, col2, col3 = st.columns(3)
    
#     with col1:
#         st.metric(label="Total Documents", value=0)
    
#     with col2:
#         st.metric(label="Total Tags", value=0)
    
#     with col3:
#         st.metric(label="Storage Used (MB)", value=0)
    
#     # Charts section
#     st.subheader("Analytics")
    
#     tab1, tab2, tab3 = st.tabs(["Documents Over Time", "Tags Distribution", "File Sizes"])
    
#     with tab1:
#         st.write("Documents uploaded over time chart will appear here")
#         # TODO: Add chart logic
    
#     with tab2:
#         st.write("Tags distribution chart will appear here")
#         # TODO: Add chart logic
    
#     with tab3:
#         st.write("File sizes chart will appear here")
#         # TODO: Add chart logic
