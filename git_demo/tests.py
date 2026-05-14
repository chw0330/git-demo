from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from posts.models import Post


class ProjectHealthTests(SimpleTestCase):
    def test_admin_url_resolves(self):
        self.assertEqual(reverse("admin:index"), "/admin/")


class PostTests(TestCase):
    def test_homepage_creates_and_lists_post(self):
        response = self.client.post(
            reverse("post_list"),
            {
                "author": "小明",
                "title": "第一条消息",
                "content": "你好，Django。",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.count(), 1)
        self.assertContains(response, "第一条消息")
        self.assertContains(response, "你好，Django。")
