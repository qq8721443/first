from django.db import models
from django.urls import reverse

from .fields import ThumbnailImageField

class Photolog(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    content = models.TextField('Photolog', blank=True)
    create_dt = models.DateTimeField('Create Date', auto_now_add=True)
    modify_dt = models.DateTimeField('Modify Date', auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))

class Photo(models.Model):
    photolog = models.ForeignKey(Photolog, on_delete=models.CASCADE, null=True)
    description = models.TextField('Photo Description', blank=True)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    upload_dt = models.DateTimeField('Upload Date', auto_now_add=True)

    class Meta:
        ordering = ('id',)
