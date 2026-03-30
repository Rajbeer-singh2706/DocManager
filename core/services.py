
class DocumentService:
    def __init__(self):
        self.repo = None 
        self.file_manager = self.file_manager

    def upload_document(self, file, tags, description, lecture_date):
        """Handle document upload logic."""

        # 1. save File 
        file_path  = self.