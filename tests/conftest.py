"""Pytest configuration and shared fixtures."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def sample_document():
    """Fixture for sample document data."""
    return {
        "name": "sample.pdf",
        "path": "/tmp/sample.pdf",
        "tags": ["lecture", "notes"],
        "description": "Sample lecture notes",
        "date": "2026-03-30"
    }


@pytest.fixture
def document_service():
    """Fixture for DocumentService."""
    from service.document_service import DocumentService
    return DocumentService()
