from django.shortcuts import render
from .models import Todo
from django.views.generic import (
    ListView
)


class TodoListView(ListView):
    queryset = Todo.objects.filter(finish=False)  # 指定查詢條件
