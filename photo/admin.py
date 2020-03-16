from django.contrib import admin
from .models import Photo, Photolog

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 2

@admin.register(Photolog)
class PhotologAdmin(admin.ModelAdmin):
    inlines = (PhotoInline,)
    list_display = ('id', 'name', 'description', 'content')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload_dt')
