from django.db import models

# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=50)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.header
