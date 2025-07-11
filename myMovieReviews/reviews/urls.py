from django.urls import path
from . import views
from .views import (
    ReviewListView, ReviewDetailView,
    ReviewCreateView, ReviewUpdateView, ReviewDeleteView
)


urlpatterns = [
    path('', views.ReviewListView.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('review/new/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_edit'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]
