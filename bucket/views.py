from django.shortcuts import render
from django.views.generic import ListView
from .models import Bucket

# Create your views here.
class bucket_list(ListView):
    model = Bucket
    template_name = 'bucket/bucket_list.html'
    context_object_name = 'buckets'
