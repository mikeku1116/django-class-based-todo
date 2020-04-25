from django.shortcuts import render
from .models import Todo
from .forms import TodoModelForm
from django.views.generic import (
    ListView,
    CreateView
)


class TodoListView(ListView):
    queryset = Todo.objects.filter(finish=False)  # 指定查詢條件

    # 要傳遞的資料
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TodoModelForm()
        return context

    # POST請求時所要做的事情
    def post(self, request, *args, **kwargs):
        return TodoCreateView.as_view()(request)


class TodoCreateView(CreateView):
    model = Todo
    fields = ['title']  # 要顯示及儲存的欄位
    success_url = '/todo'  # 儲存成功後要導向的網址
