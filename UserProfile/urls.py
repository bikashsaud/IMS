from django.urls import path
# from CMS.views import base,agentsignin,signup,signout,agent,client,clientsignin
from . import views

# app_name='UserProfile'

urlpatterns = [
    path('signin/', views.signin,name='login'),
    path('register/', views.register,name='register'),
    path('signout/', views.signout,name='logout'),

]
