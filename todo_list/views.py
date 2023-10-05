from django.shortcuts import render
from django.views import generic

from todo_list.models import Tag


def index(request):
    return render(request, "todo_list/index.html")


class TagListView(generic.ListView):
    model = Tag
