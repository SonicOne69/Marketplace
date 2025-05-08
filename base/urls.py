from django.urls import path 
from . import views
urlpatterns = [
    path('', views.main, name='main'),
    path('create_post/', views.create_post, name='create_post'),
    path('search/', views.search, name='search'),
    path('categories/<str:category>', views.categories, name='categories'),
    path('post/<str:postname>', views.post_page, name='post_page'),
    path('chat/<str:chatname>', views.chat, name='chat'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]