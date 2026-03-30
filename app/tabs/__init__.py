"""Tab modules for DocManager application."""

from .upload_tab import render_upload_tab
from .search_tab import render_search_tab
from .analytics_tab import render_analytics_tab

__all__ = ["render_upload_tab", "render_search_tab", "render_analytics_tab"]
