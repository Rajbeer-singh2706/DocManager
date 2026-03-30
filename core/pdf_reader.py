import pymupdf, os 

OUTPUT_DIR = os.path.join('storage', 'pdfs')

class PDFReader:
    """Class to handle PDF reading and text extraction."""
    
    def __init__(self):
        pass

    def convert_pdf_to_images(self,file_path): 
        """Convert PDF pages to images."""
        # You can use libraries like PyMuPDF, pdf2image, or similar to convert PDF pages to images
        # c://hello/user/a/a.pdf
        # a.pdf
        # .pdf --> '' -> a

        doc = pymupdf.open(file_path)
        folder_name = os.path.basename(file_path).replace('.pdf', '')
        output_folder = os.path.join(OUTPUT_DIR, folder_name)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        image_paths = []
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            matrix = pymupdf.Matrix(2, 2)  # Scale factor for better resolution
            pix = page.get_pixmap(matrix=matrix)
            image_path = os.path.join(output_folder, f'page_{page_num}.png')
            pix.save(image_path)
            image_paths.append(image_path)

        # Conversion logic would go here
        doc.close()
        return image_paths