from django.urls import path

from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_home"),
    path('post/<int:pk>/', BlogDetailView.as_view(), name="blog_post_detail")
]