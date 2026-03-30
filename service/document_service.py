
from core.file_manager import FileManager
from core.thumbnail import ThumbnailGenerator

class DocumentService:
    def __init__(self):
        self.repo = None 
        self.file_manager = FileManager()
        self.thumbnail_generator = ThumbnailGenerator()
        #self.reader = PDFReader()

    def upload_document(self, uploaded_file, tags, description, lecture_date):
        """Handle document upload logic."""

        # 1. save File 
        file_path  = self.file_manager.save_file(uploaded_file)

        # 2. generate thumbnail
        thumbnail_path = self.thumbnail_generator.generate_thumbnail(file_path)

        # 3. Get total Pages
        total_pages = self.thumbnail_generator.get_total_pages(file_path)

        # 4. convert to images 
