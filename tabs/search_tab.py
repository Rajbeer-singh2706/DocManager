"""Search Tab - Search and filter documents."""

import os
import streamlit as st
from service.document_service import DocumentService
from service.analytic_service import AnalyticService

#document_service = DocumentService()
#AnalyticService() = AnalyticService()

## When it renders first time, it should not show any results, 
## so we initialize it with empty list

if 'search_results' not in st.session_state:
    st.session_state.search_results = []

if 'reader_mode' not in st.session_state:
    st.session_state.reader_mode = False

if 'selected_doc' not in st.session_state:
    st.session_state.selected_doc = None

if 'current_page' not in st.session_state:
    st.session_state.current_page = 0

# st.session_state.search_results = []
# st.session_state.reader_mode = False
# st.session_state.selected_doc = None 
    
def render_search_tab():
        st.header("Search your PDF documents")
        print(f"st.session_state.reader_mode: {st.session_state.reader_mode}")
        print(f"st.session_state.selected_doc: {st.session_state.selected_doc}")

        col1, col2 = st.columns(2)

        with col1:
            search_tag = st.text_input("Search by tag")
        
        with col2:
            search_date = st.date_input("Search by date", value=None)
        
        if st.button("Search", key="search_btn"):
            AnalyticService.record_app_visit("search_document")
            st.session_state.search_results = DocumentService().search_documents(
                tag=search_tag if search_tag else None,
                date=str(search_date) if search_date else None
            )
        
        results = st.session_state.search_results
        print("here ", results) 

        ### Display search results
        if results and not st.session_state.reader_mode:
            st.subheader(f"Found {len(results)} document(s) matching the search criteria:")
            container = st.container(height=400)
            with container:
                for doc in results:
                    print(doc)
                    # doc --> obj of document from models.py 
                    col1 , col2 = st.columns([1,3])
                    # 4 --> 25% left, right --> 75%
                    with col1:
                        if doc.thumbnail_path:
                            st.image(doc.thumbnail_path, width=120)
                    
                    with col2:
                        st.markdown(f"**Name:** {doc.name}")
                        st.markdown(f"**Description:** {doc.description}")
                        st.markdown(f"**Tags:** {doc.tags}")
                        st.markdown(f"**Upload Date:** {doc.upload_date}")
                        st.markdown(f"**Lecture Date:** {doc.lecture_date}")
                        st.markdown(f"**Total Pages:** {doc.total_pages}")

                        ## Now Data is displayed , we want to implement one more feature that is OPEN
                        ## Whenever user clicks on OPEN button, it restart the app and open in READER MODE 

                        if st.button("Open", key=f"open_{doc.id}"):
                            AnalyticService.record_app_visit("open_document")
                            st.session_state.selected_doc = doc 
                            st.session_state.current_page = 0 
                            st.session_state.reader_mode = True
                            st.rerun()

                        st.markdown("---")

        ### WHen User click on OPEN button, it will open the document in reader mode
        if st.session_state.reader_mode and st.session_state.selected_doc:
            print("Opening document in reader mode:", st.session_state.reader_mode)
            st.write("Reader Mode Activated")

            doc = st.session_state.selected_doc
            st.subheader(f"📖 Reading: {doc.name}")


            folder_name = os.path.basename(doc.path).replace(".pdf", "")
            image_dir = os.path.join("storage", "pdfs", folder_name)

            st.write("Image dir: ", image_dir)
            st.write("Files: ", os.listdir(image_dir) if os.path.exists(image_dir) else "Directory not found")

            if not os.path.exists(image_dir):
                st.error("Images not found, PDF conversion failed.")
            else:
                images = sorted(os.listdir(image_dir))

                # total Pages = len(images)
                total_pages = doc.total_pages
                current_page = st.session_state.current_page

                col1, col2, col3 = st.columns([1,2,1])

                ### Previous BUTTON 
                with col1:
                    if st.button("⬅ Previous") and current_page > 0:
                        AnalyticService.record_app_visit("prev_page")
                        st.session_state.current_page -=1
                        st.rerun()
                
                ## NEXT BUTTON 
                with col3:
                    if st.button("Next ➡") and current_page < total_pages -1:
                        AnalyticService.record_app_visit("next_page")
                        st.session_state.current_page +=1
                        st.rerun()

                ## Display Current Page
                img_path = os.path.join(image_dir, images[st.session_state.current_page])
                st.image(img_path, width="stretch")

                ## Show the Progress 
                ## Records Page visit analytics
                AnalyticService.record_page_visit(doc.id,current_page)
                unique_pages_viewed = AnalyticService.get_unique_pages_viewed(doc.id)

                progress = (unique_pages_viewed / doc.total_pages) * 100 if doc.total_pages else 0 
                st.progress(progress/100)

                st.write(f"Progress: {progress:.2f}% ({unique_pages_viewed} / {doc.total_pages})")


            #
            if st.button("Close Reader"):
                AnalyticService.record_app_visit("close_reader")
                st.session_state.reader_mode = False
                st.rerun()


### IF we want to define into class then we need to remove st.session-state from instance , it suld be class variable if we want to create 
## Bocz everytime we run st.rerun() ---> new instance of searchTab() is created and it will reset all the instance variables, so we need 
# to make it class variable or we can keep it outside of class as global variable.


## Once reader mode is closed --> its back to same state , where it has the search results and user can open any document 
# from search results.