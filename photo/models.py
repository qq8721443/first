from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from .fields import ThumbnailImageField

class Photolog(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    content = RichTextUploadingField()
    create_dt = models.DateTimeField('Create Date', auto_now_add=True)
    modify_dt = models.DateTimeField('Modify Date', auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='OWNER', null=True, blank=True)

    class Meta:
        ordering = ('-create_dt','name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:photolog_detail', args=(self.id,))

class Photo(models.Model):
    photolog = models.ForeignKey(Photolog, on_delete=models.CASCADE, related_name='photos', null=True)
    description = models.TextField('Photo Description', blank=True)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    upload_dt = models.DateTimeField('Upload Date', auto_now_add=True)

    class Meta:
        ordering = ('id',)
