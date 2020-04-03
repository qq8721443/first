from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Bucket
from django import forms

# Create your views here.
class bucket_list(ListView):
    model = Bucket
    template_name = 'bucket/bucket_list.html'
    context_object_name = 'buckets'

class bucketCV(CreateView):
    model = Bucket
    #template_name = 'Post/post_form.html' 그냥 자동으로 _form.html로 가는듯
    fields = ['title', 'content']
    success_url = reverse_lazy('bucket:bucket')

    class Meta:
        widgets = {
            'title':forms.TextInput(),
            'content':forms.TextInput(),
        }

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
