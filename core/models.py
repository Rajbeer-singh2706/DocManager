class Document:
    """Class to represent a document with its metadata."""
    def __init__(self,
        id,
        name,
        path,
        thumbnail_path,
        tags,
        description,
        upload_date,
        lecture_date,
        total_pages
):
        self.id = id 
        self.name = name 
        self.path = path 
        self.thumbnail_path = thumbnail_path
        self.tags = tags
        self.description = description
        self.lecture_date = lecture_date
        self.upload_date = upload_date
        self.total_pages = total_pages
