from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from todo_list.models import Tag


def index(request):
    return render(request, "todo_list/index.html")


class TagListView(generic.ListView):
    model = Tag


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")
