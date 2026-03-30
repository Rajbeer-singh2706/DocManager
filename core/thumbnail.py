import os
import pymupdf 

THUMBNAIL_DIR = os.path.join("storage", "thumbnails")

class ThumbnailGenerator:
    """Class to generate thumbnails for PDF documents."""

    def __init__(self):
        # Ensure thumbnail directory exists
        if not os.path.exists(THUMBNAIL_DIR):
            os.makedirs(THUMBNAIL_DIR)

    def generate_thumbnail(self, file_path):
        """Generate a thumbnail for the given PDF file."""
        # You can use libraries like PyMuPDF, pdf2image, or similar to create thumbnails
        doc = pymupdf.open(file_path)

        # Load the first page
        page = doc.load_page(0) 
        pix = page.get_pixmap() # low resolution thumbnail
        base_name =os.path.basename(file_path).replace('.pdf', '.png')
        # c://hello/user/a/a.pdf
        # a.pdf
        # a.png
        thumb_path = os.path.join(THUMBNAIL_DIR, base_name)
        pix.save(thumb_path)
        doc.close()
        return thumb_path
    

    def get_total_pages(self,file_path):
        """Get total number of pages in the PDF."""
        doc = pymupdf.open(file_path)
        total_pages = doc.page_count
        # total = len(doc)
        doc.close()
        return total_pages
