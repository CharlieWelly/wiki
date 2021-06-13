from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry_page, name="entry_page"),
    path("search/", views.search, name="search"),
    path("new_page/", views.NewPage.as_view(), name="new_page"),
    path("edit_page/", views.EditPage.as_view(), name="edit_page"),
    path("random_page/", views.random_page, name="random_page"),
]
