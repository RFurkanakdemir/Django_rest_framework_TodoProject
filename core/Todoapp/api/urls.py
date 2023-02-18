from django.urls import path,include
from Todoapp.api import views as api_views



urlpatterns = [
    path('tasks/',api_views.TaskListCreateAPIView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', api_views.TaskDetailAPIView.as_view(), name= 'task-detail'),
    path('users/',api_views.UserListAPIVİEW.as_view(),name='users'),
    path('categories/',api_views.CategorieListCreateAPIView.as_view(),name='categories'),
    path('categories/<int:pk>/',api_views.CategorieDetailAPIView.as_view(),name='Categorie-detail')

]