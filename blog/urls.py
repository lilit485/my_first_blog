from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new1/', views.post_new1, name='post_new1'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout",views.logout_request, name="logout"),




]