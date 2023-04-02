from django.db import models

class User(models.Model):
    nick_name = models.CharField(max_length=254)
    host_name = models.CharField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    def __str__(self):
        """String representing Model object"""
        return f"{self.first_name} {self.last_name}"
