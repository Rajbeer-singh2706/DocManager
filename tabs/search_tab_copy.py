"""Search Tab - Search and filter documents."""

import streamlit as st
from service.document_service import DocumentService

class SearchTab:
    """Class to handle the search tab functionality."""

    def __init__(self, st):
        self.document_service = DocumentService()
        self.st = st
        self.st.session_state.search_results = []
        self.st.session_state.reader_mode = False
        self.st.session_state.selected_doc = None 
    
    def render_search_tab(self):
        self.st.header("Search your PDF documents")
        print(f"self.st.session_state.reader_mode: {self.st.session_state.reader_mode}")
        print(f"self.st.session_state.selected_doc: {self.st.session_state.selected_doc}")
        
        col1, col2 = self.st.columns(2)

        with col1:
            search_tag = self.st.text_input("Search by tag")
        
        with col2:
            search_date = self.st.date_input("Search by date", value=None)
        
        if self.st.button("Search", key="search_btn"):
            self.st.session_state.search_results = self.document_service.search_documents(
                tag=search_tag if search_tag else None,
                date=str(search_date) if search_date else None
            )
        
        results = self.st.session_state.search_results
        print("here ", results) 

        ### Display search results
        if results and not self.st.session_state.reader_mode:
            self.st.subheader(f"Found {len(results)} document(s) matching the search criteria:")
            container = self.st.container(height=400)
            with container:
                for doc in results:
                    print(doc)
                    # doc --> obj of document from models.py 
                    col1 , col2 = self.st.columns([1,3])
                    # 4 --> 25% left, right --> 75%
                    with col1:
                        if doc.thumbnail_path:
                            self.st.image(doc.thumbnail_path, width=120)
                    
                    with col2:
                        self.st.markdown(f"**Name:** {doc.name}")
                        self.st.markdown(f"**Description:** {doc.description}")
                        self.st.markdown(f"**Tags:** {doc.tags}")
                        self.st.markdown(f"**Upload Date:** {doc.upload_date}")
                        self.st.markdown(f"**Lecture Date:** {doc.lecture_date}")
                        self.st.markdown(f"**Total Pages:** {doc.total_pages}")
                        self.st.markdown("---")

                        ## Now Data is displayed , we want to implement one more feature that is OPEN
                        ## Whenever user clicks on OPEN button, it restart the app and open in READER MODE 

                        if self.st.button("Open", key=f"open_{doc.id}"):
                            self.st.session_state.selected_doc = doc 
                            self.st.session_state.current_page = 0 
                            self.st.session_state.reader_mode = True
                            self.st.rerun()

        if self.st.session_state.reader_mode and self.st.session_state.selected_doc:
            print("Opening document in reader mode:", self.st.session_state.selected_doc)



