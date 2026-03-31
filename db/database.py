import sqlite3
import os 

DB_PATH = os.path.join("data", "documents.db")

class DatabaseManager:
    def __init__(self, db_path=DB_PATH):
        self.db_path = db_path
        self._connect()

    def init_db(self):
        """Initialize the database and create necessary tables."""
        self._create_tables()

    def _connect(self):
        """Establish a connection to the SQLite database."""
        try:
            self.conn = sqlite3.connect(self.db_path)
            print(f"Connected to database at {self.db_path}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def _create_tables(self):
        """Create necessary tables if they don't exist."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS documents (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    path TEXT,
                    thumbnail_path TEXT,
                    tags TEXT,
                    description TEXT,
                    upload_date TEXT,
                    lecture_date TEXT,
                    total_pages INTEGER
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS page_visits(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    document_id INTEGER,
                    page_number INTEGER,
                    timestamp TEXT       
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS app_visits(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_type TEXT,
                    timestamp TEXT       
                )
            """)

            self.conn.commit()
            print("Tables created successfully")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            print("Database connection closed")


# ### INitialize DB 
# def init_db():
#     db = DatabaseManager()
#     db.close()
