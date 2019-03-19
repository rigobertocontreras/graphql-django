from django.test import TestCase
from graphene.test import Client
from graphql_django.server.models import Post
from graphql_django.server.schema import create_schema


class PostTestCase(TestCase):
    def setUp(self):
        Post.objects.create(title="title test")

    def test_slug(self):
        """Post slugify test"""
        post_test = Post.objects.get(title="title test")
        self.assertEqual(post_test.slug, "title-test")


class SchemaTest(TestCase):
    def setUp(self):
        self.client = Client(create_schema())

    def test_schema(self):
        executed = self.client.execute('''{ post(id:"1"){id} }''')
        self.assertEqual(executed, {"data": {
            "post": None
        }})

    def test_user(self):
        executed = self.client.execute('''{ user(id:"1"){id} }''')
        self.assertEqual(executed, {"data": {
            "user": {"id": "1"}
        }})

    def test_user_not_included(self):
        local_client = Client(create_schema(expose_user=False))
        executed = local_client.execute('''{user(id:"1"){id}}''')
        error = {'errors':
                 [{'locations': [{'column': 2, 'line': 1}],
                   'message': 'Cannot query field "user" on type "Query".'}]}
        self.assertEqual((executed), error)
