"""Post application module."""

from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Posts  aplication seettings."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    varbose_name = 'Posts'
    
