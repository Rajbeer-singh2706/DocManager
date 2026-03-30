
from core.file_manager import FileManager

class DocumentService:
    def __init__(self):
        self.repo = None 
        self.file_manager = FileManager()

    def upload_document(self, uploaded_file, tags, description, lecture_date):
        """Handle document upload logic."""

        # 1. save File 
        file_path  = self.file_manager.save_file(uploaded_file)