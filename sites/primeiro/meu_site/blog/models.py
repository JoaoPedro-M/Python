from django.db import models


class Post(models.Model):
    header = models.CharField(max_length=50)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.header
