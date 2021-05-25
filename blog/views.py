from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "blog_home.html"
    context_object_name = "all_posts_list"

class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_post_detail.html"
    context_object_name = "post"

class BlogCreateView(CreateView):
    model = Post
    template_name = "blog_post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "blog_post_edit.html"
    fields = ["title", "body"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = "blog_post_delete.html"
    success_url = reverse_lazy("blog_home")