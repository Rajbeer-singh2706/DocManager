from datetime import datetime
from db.database import DatabaseManager

class AnalyticService:
    def __init__(self):
        # Initialize your database connection here
        self.db_manager = DatabaseManager()
        self.connection = self.db_manager.conn

    def record_app_visit(self, event_type):
        """Record an application visit event."""
        cursor = self.connection.cursor()

        cursor.execute("""
        INSERT INTO app_visits (event_type, timestamp)
        VALUES (?, ?)
        """, (
                event_type, datetime.now().isoformat()
             )
        )
        self.connection.commit()
        self.db_manager.close()

    def get_app_visits(self):
        """Get application visit data."""
        cursor = self.connection.cursor() 

        cursor.execute("""
            SELECT 
                        event_type, COUNT(*) as event_count 
            FROM app_visits
            GROUP BY event_type        
        """)

        rows = cursor.fetchall()
        self.db_manager.close()
        return rows 

    def get_unique_pages_viewed(self,document_id):
        """Get the number of unique pages viewed for a document."""
        cursor = self.connection.cursor()

        cursor.execute("""
            SELECT COUNT(DISTINCT page_number) 
            FROM page_visits
            WHERE document_id = ?
        """, (document_id,))

        result = cursor.fetchone()
        self.db_manager.close()
        return result[0] if result else 0

        

## Table Name : page_visits or page_views