from django.db import models
from users.models import User

class Article(models.Model):
    title = models.CharField(max_length=254)
    description = models.CharField(max_length=254)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    article_body = models.CharField(max_length=254)

    def __str__(self):
        """String representing Model object"""
        return f"{self.title} {self.author} {self.created_at}"


    class Meta:
        ordering = ['-created_at']