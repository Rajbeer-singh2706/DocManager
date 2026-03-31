"""Upload Tab - Handle PDF document uploads with metadata."""

from service.document_service import DocumentService
from service.analytic_service import AnalyticService

    
#import streamlit as st 

class UploadTab:
    """Class to handle the upload tab functionality."""

    def __init__(self, st):
        self.document_service = DocumentService()
        self.analytics_service = AnalyticService() 
        self.st = st

    def render_upload_tab(self):
        """Render the upload tab interface."""
        self.st.write("Upload your PDF document here")

        # File upload
        uploaded_file = self.st.file_uploader("Choose a PDF file", type=["pdf"])

        # Document metadata
        self.st.subheader("Document Details")
        tags = self.st.text_input("Enter tags for the document (comma separated)")
        description = self.st.text_area("Enter a description for the document")
        lecture_date = self.st.date_input("Select the lecture date", value = None )

        if uploaded_file:
            self.st.success(f"File selected: {uploaded_file.name}")
            self.st.write(f"File size: {uploaded_file.size} bytes")

        # Submit button
        if self.st.button("Upload Document", key="upload_btn"):
            if uploaded_file:
                self.document_service.upload_document(uploaded_file, tags, description, lecture_date)
                self.analytics_service.record_app_visit("document_uploaded")
                self.st.success("Document uploaded successfully!")
            else:
                self.st.error("Please fill in all fields")


## check this as a decorator for all buttons 
## self.analytics_service.record_app_visit("document_uploaded")