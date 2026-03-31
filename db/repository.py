
from core.models import Document
from db.database import DatabaseManager

class DocumentRepository:
    def __init__(self):
        # Initialize your database connection here
        pass 
    
    def add_document(self, document: Document):
        # Implement logic to add a document to the database
        db_manager = DatabaseManager()
        connection = db_manager.conn
        cursor = connection.cursor()
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
        connection.commit()
        db_manager.close()

    def search_documents(self,tag=None, date = None ):
        db_manager = DatabaseManager()
        connection = db_manager.conn
        cursor = connection.cursor()
        query = "SELECT * FROM documents"

        conditions = []
        params = []

        ##  WHERE , OR 

        if tag:
            conditions.append("tags LIKE ?")
            params.append(f"%{tag}%")
        
        if date:
            conditions.append("lecture_date = ?")
            params.append(date)

        if conditions: 
            query += " WHERE " + " OR ".join(conditions)
        
        print("Executing query:", query)
        cursor.execute(query, params)
        rows = cursor.fetchall()
        db_manager.close()

        ## List of documents objects
        return [Document(*row) for row in rows]

    def get_all_documents(self):
        db_manager = DatabaseManager()
        connection = db_manager.conn
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM documents")
        rows = cursor.fetchall()
        db_manager.close()

        return [Document(*row) for row in rows]

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
    #     pas