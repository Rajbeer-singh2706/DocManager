from datetime import datetime
from db.database import DatabaseManager

class AnalyticService:
    @staticmethod
    def record_page_visit(document_id, page_number):
        """Record a page visit event."""
        db_manager = DatabaseManager()
        connection = db_manager.conn
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO page_visits (document_id, page_number, timestamp)
        VALUES (?, ?, ?)
        """, (
                document_id, page_number, datetime.now().isoformat()
             )
        )
        connection.commit()
        db_manager.close()

    @staticmethod
    def record_app_visit(event_type):
        """Record an application visit event."""
        db_manager = DatabaseManager()
        connection = db_manager.conn
        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO app_visits (event_type, timestamp)
        VALUES (?, ?)
        """, (
                event_type, datetime.now().isoformat()
             )
        )
        connection.commit()
        db_manager.close()

    @staticmethod
    def get_app_visits():
        """Get application visit data."""
        db_manager = DatabaseManager()
        connection = db_manager.conn
        cursor = connection.cursor()

        cursor.execute("""
            SELECT 
                        event_type, COUNT(*) as event_count 
            FROM app_visits
            GROUP BY event_type        
        """)

        rows = cursor.fetchall()
        db_manager.close()
        return rows 

    @staticmethod
    def get_unique_pages_viewed(document_id):
        """Get the number of unique pages viewed for a document."""
        db_manager = DatabaseManager()
        connection = db_manager.conn
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COUNT(DISTINCT page_number) 
            FROM page_visits
            WHERE document_id = ?
        """, (document_id,))

        result = cursor.fetchone()
        db_manager.close()
        return result[0] if result else 0

    @staticmethod
    def reset_analytics():
        """Reset all analytics data."""
        db_manager = DatabaseManager()
        connection = db_manager.conn
        cursor = connection.cursor()

        cursor.execute("DELETE FROM page_visits")
        cursor.execute("DELETE FROM app_visits")

        #cursor.execute("truncate TABLE page_visits")
        #cursor.execute("truncate app_visits")

        connection.commit()
        db_manager.close()

## Table Name : page_visits or page_views
## Here is one problem , if we create a object --> one connection will be created and it will be closed after one method call, 
# so we need to create connection for each method call and close it after that, otherwise we can create connection in init and 
# close it in destructor but it is not recommended way because if we forget to close the connection then it will lead to memory leak,
#  so better way is to create connection for each method call and close it after that.