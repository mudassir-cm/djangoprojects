from django.urls import path
from blog import views

urlpatterns = [
    path('about/', views.about),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('signup/', views.user_signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('addpost/', views.addpost, name="addpost"),
    path('updatepost/<int:id>', views.updatepost, name="updatepost"),
    path('deletepost/<int:id>', views.deletepost, name="deletepost"),
]