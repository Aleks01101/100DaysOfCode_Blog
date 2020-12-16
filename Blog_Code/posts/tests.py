from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='testuser1',password='abc123')
        testuser1.save()

        testpost = Post.objects.create(author=testuser1, title='test', body='body content..')
        testpost.save()

    def testblog_test(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author,'testuser1')
        self.assertEqual(title,'test')
        self.assertEqual(body,'body content..')