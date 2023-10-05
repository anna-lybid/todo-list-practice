from django.urls import path

from todo_list.views import index, TagListView

urlpatterns = [
    path("", index, name="todo-index"),
    path("tags/", TagListView.as_view(), name="tags"),
]
