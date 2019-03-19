from django.test import TestCase
from graphql_django.server.models import Post


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="title test")

    def test_slug(self):
        """Post slugify test"""
        post_test = Post.objects.get(title="title test")
        self.assertEqual(post_test.slug, "title-test")
