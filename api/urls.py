from django.urls import path
from .views import *

urlpatterns = [
    path('book-list',BookListView.as_view()),
    path('book-create',BookCreateView.as_view()),
    path('book-edit/<int:pk>',BookUpdateView.as_view()),
    path('book-delete/<int:pk>',BookDeleteView.as_view()),

    path('author-list',AuthorListView.as_view()),
    path('author-create',AuthorCreateView.as_view()),
    path('author-edit/<int:pk>',AuthorUpdateView.as_view()),
    path('author-delete/<int:pk>',AuthorDeleteView.as_view()),
]
