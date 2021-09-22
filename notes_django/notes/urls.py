from django.urls import path
from . import views

urlpatterns = [
    path('', views.NotesView.as_view(), name='user_home'),
    path('create/', views.NotesCreateView.as_view(), name='create'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout')
]
