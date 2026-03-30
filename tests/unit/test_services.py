"""Unit tests for core services."""

import pytest
from service.document_service import DocumentService


class TestDocumentService:
    """Tests for DocumentService class."""

    def test_document_service_initialization(self, document_service):
        """Test that DocumentService initializes correctly."""
        assert document_service is not None
        assert isinstance(document_service, DocumentService)

    def test_document_service_has_methods(self, document_service):
        """Test that DocumentService has expected methods."""
        # Add your service methods here as they're implemented
        assert hasattr(document_service, '__class__')

    def test_sample_with_fixture(self, sample_document):
        """Example test using the sample_document fixture."""
        assert sample_document["name"] == "sample.pdf"
        assert "lecture" in sample_document["tags"]
