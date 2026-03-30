
from core.models import Document
from db.database import DatabaseManager

class DocumentRepository:
    def __init__(self):
        # Initialize your database connection here
        self.db_manager = DatabaseManager()
        self.connection = self.db_manager.conn
    
    def add_document(self, document: Document):
        # Implement logic to add a document to the database
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO documents(
                       name, path, thumbnail_path, tags, description, upload_date, lecture_date, total_pages
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            document.name,
            document.path,
            document.thumbnail_path,
            document.tags,
            document.description,
            document.upload_date,
            document.lecture_date,
            document.total_pages
        )
        )
        self.connection.commit()
        self.db_manager.close()

        

    # def save_document(self, document_data):
    #     # Implement logic to save document data to the database
    #     pass

    # def get_document(self, document_id):
    #     # Implement logic to retrieve a document by its ID
    #     pass

    # def search_documents(self, query):
    #     # Implement logic to search for documents based on a query
    #     pass

    # def delete_document(self, document_id):
    #     # Implement logic to delete a document by its ID
    #     pass