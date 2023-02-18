from rest_framework import generics
from Todoapp.models import Task,Categorie
from Todoapp.api.serializers import TaskSerializer,UserSerializer,CategorieSerializer
from rest_framework import permissions
from Todoapp.api.permissions import IsTaskUser
from django.contrib.auth.models import User,AnonymousUser
from rest_framework import status
from rest_framework.response import Response



class TaskListCreateAPIView(generics.ListCreateAPIView):
    
    def get_queryset(self):
    
        user = self.request.user
        if self.request.user.is_anonymous:
            raise TypeError(
            "User is not found"
        )
            
        return Task.objects.filter(owner=user)
            
       


    serializer_class=TaskSerializer
    
    def perform_create(self, serializer):
        serializer.save( owner = self.request.user)


class TaskDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Task.objects.filter(owner=user)
    serializer_class=TaskSerializer
    permission_classes=[IsTaskUser]


class UserListAPIVİEW(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAdminUser]




class CategorieListCreateAPIView (generics.ListCreateAPIView):
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Categorie.objects.filter(owner=user)
    serializer_class=CategorieSerializer
    
    def perform_create(self, serializer):
        serializer.save( owner = self.request.user)


class CategorieDetailAPIView ( generics.RetrieveUpdateDestroyAPIView):
    queryset = Categorie
        
    serializer_class=CategorieSerializer
    permission_classes=[IsTaskUser]