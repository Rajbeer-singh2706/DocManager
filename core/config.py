"""Configuration and constants for DocManager application."""

from enum import Enum
from pathlib import Path
import os


class Config:
    """Central configuration class for all application constants."""
    
    # Base paths
    BASE_DIR = Path(__file__).parent.parent
    DATA_DIR = BASE_DIR / "data"
    DB_DIR = BASE_DIR / "db"
    LOGS_DIR = BASE_DIR / "logs"
    
    # Storage directories
    PDF_STORAGE_DIR = DATA_DIR / "pdfs"
    UPLOADS_TEMP_DIR = DATA_DIR / "uploads_temp"
    BACKUPS_DIR = DATA_DIR / "backups"
    
    # File size limits (in MB)
    MAX_PDF_SIZE = 50  # MB
    MAX_UPLOAD_SIZE = 100  # MB
    
    # Supported file types
    ALLOWED_FILE_TYPES = ["pdf"]
    
    # Database
    DATABASE_PATH = DB_DIR / "docmanager.db"
    DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
    
    # Application settings
    APP_NAME = "Smart PDF Document Manager"
    APP_VERSION = "1.0.0"
    DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"
    
    # Pagination
    ITEMS_PER_PAGE = 10
    
    # Tag settings
    MAX_TAGS = 10
    MAX_TAG_LENGTH = 50
    
    # Search settings
    SEARCH_RESULT_LIMIT = 100
    
    @classmethod
    def create_directories(cls):
        """Create all necessary directories if they don't exist."""
        directories = [
            cls.DATA_DIR,
            cls.DB_DIR,
            cls.LOGS_DIR,
            cls.PDF_STORAGE_DIR,
            cls.UPLOADS_TEMP_DIR,
            cls.BACKUPS_DIR,
        ]
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)


class DocumentStatus(Enum):
    """Enum for document status."""
    
    DRAFT = "draft"
    UPLOADED = "uploaded"
    PROCESSED = "processed"
    ARCHIVED = "archived"
    DELETED = "deleted"


class SearchType(Enum):
    """Enum for search type."""
    
    TITLE = "title"
    TAGS = "tags"
    DESCRIPTION = "description"
    DATE = "date"
    KEYWORD = "keyword"


class SortOrder(Enum):
    """Enum for sort order."""
    
    ASCENDING = "asc"
    DESCENDING = "desc"


# Initialize directories on import
Config.create_directories()
