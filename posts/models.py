from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=40)
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
