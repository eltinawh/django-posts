from django.urls import path
from posts.views import (
    post_list_and_create,
    load_post_data_view
)

app_name = "posts"

urlpatterns = [
    path("", post_list_and_create, name="main-board"),
    path("data/<int:max_idx>/", load_post_data_view, name="posts-data"),
]