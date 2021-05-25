from unittest.case import expectedFailure
from django.test import TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.
class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text="mensaje de prueba")
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.text}"
        self.assertEqual(expected_object_name, "mensaje de prueba")


class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text="Esto es otra prueba")
    
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get("posts/")
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse("posts_home"))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse("posts_home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "posts_home.html")
