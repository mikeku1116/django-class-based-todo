from django.urls import path
from .views import TodoListView, TodoCreateView, TodoUpdateView

app_name = 'todo'
urlpatterns = [
    path('', TodoListView.as_view(), name='list'),
    path('create', TodoCreateView.as_view(), name='create'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='update'),
]
