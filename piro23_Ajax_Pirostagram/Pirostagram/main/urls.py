from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('new/', views.post_new, name='post_new'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('comment_create/<int:post_id>/', views.comment_create, name='comment_create'),
    path('comment_delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('post_delete/<int:post_id>/', views.post_delete, name='post_delete'),
]