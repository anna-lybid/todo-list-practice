from django.urls import path

from todo_list.views import index, TagListView, TagUpdateView, TagDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete")
]


app_name = "todo_list"
