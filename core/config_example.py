"""Example usage of Config and Enums from config.py"""

from config import Config, DocumentStatus, SearchType, SortOrder

# Example 1: Using storage directory
pdf_storage = Config.PDF_STORAGE_DIR
print(f"PDF storage directory: {pdf_storage}")

# Example 2: Using file size limit
max_size = Config.MAX_PDF_SIZE
print(f"Max PDF size: {max_size} MB")

# Example 3: Using database path
db_path = Config.DATABASE_URL
print(f"Database URL: {db_path}")

# Example 4: Using Enums
doc_status = DocumentStatus.UPLOADED
print(f"Document status: {doc_status.value}")

# Example 5: Using SearchType
search = SearchType.KEYWORD
print(f"Search type: {search.value}")

# Example 6: All constants in Config
print(f"\nAll Config paths:")
print(f"Base Dir: {Config.BASE_DIR}")
print(f"Data Dir: {Config.DATA_DIR}")
print(f"DB Dir: {Config.DB_DIR}")
print(f"PDF Storage: {Config.PDF_STORAGE_DIR}")
