from django.db import models

# Create your models here.
class Bucket(models.Model):
    title = models.CharField(verbose_name= 'TITLE', max_length=50)

    def __str__(self):
        return self.title
