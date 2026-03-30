import os 
from datetime import datetime 

PDF_STORAGE_DIR = os.path.join("storage", "pdfs")


class FileManager:
     def save_file(self, uploaded_file):
          timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
          filename = f"{timestamp}_{uploaded_file.name}"

          file_path = os.path.join(PDF_STORAGE_DIR, filename)

          # Save File   
          with open(file_path, "wb") as writer:
               writer.write(uploaded_file.read())
        
          return file_path












# class FileManager:
#     # def __init__(self, base_dir):
#     #     self.base_dir = base_dir

#     # def save_file(self, file, filename):
#     #     """Save the uploaded file to the specified location."""
#     #     save_path = os.path.join(self.base_dir, "uploads", filename)
#     #     with open(save_path, "wb") as f:
#     #         f.write(file.getbuffer())
#     #     return save_path