from datetime import datetime

from db.repository import DocumentRepository
from core.file_manager import FileManager
from core.thumbnail import ThumbnailGenerator
from core.pdf_reader import PDFReader
from core.models import Document

class DocumentService:
    def __init__(self):
        self.repo = DocumentRepository() 
        self.file_manager = FileManager()
        self.thumbnail_generator = ThumbnailGenerator()
        self.reader = PDFReader()

    def upload_document(self, uploaded_file, tags, description, lecture_date):
        """Handle document upload logic."""

        # 1. save File 
        file_path  = self.file_manager.save_file(uploaded_file)

        # 2. generate thumbnail
        thumbnail_path = self.thumbnail_generator.generate_thumbnail(file_path)

        # 3. Get total Pages
        total_pages = self.thumbnail_generator.get_total_pages(file_path)

        # 4. convert to images 
        image_paths = self.reader.convert_pdf_to_images(file_path)

        # 5. Create required variable: upload date 
        upload_date = datetime.now().strftime("%Y-%m-%d")

        # 6. create Model Object
        doc = Document(
            id = None, # will be set by the database
            name = uploaded_file.name,
            path = file_path,
            thumbnail_path = thumbnail_path,
            tags = tags,
            description = description,
            lecture_date = lecture_date,
            upload_date = upload_date,
            total_pages = total_pages
        )

        # 7. Save to DB
        self.repo.add_document(doc)
