from django.contrib import admin
from .models import Bucket
# Register your models here.


@admin.register(Bucket)
class BucketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
