"""Web Routes."""

from app.http.controllers.PageController import PageController
from masonite.routes import Get, Post

ROUTES = [
    Get("/", PageController.show),
]
