# posts/tests/test_apis.py
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()

class PostAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass123!')
        cls.post = Post.objects.create(
            title='Test Post',
            content='Test Content',
            author=cls.user
        )

    def test_post_list(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_post_creation_authenticated(self):
        self.client.force_login(self.user)
        url = reverse('post-list')
        data = {'title': 'New Post', 'content': 'New Content'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)