from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Post
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Create your views here.

class PostDV(DetailView):
    template_name = 'Post/post_detail.html'
    model = Post

class PostLV(ListView):
    template_name = 'Post/post_list.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 10

class PostCV(CreateView):
    model = Post
    #template_name = 'Post/post_form.html' 그냥 자동으로 _form.html로 가는듯
    fields = ['title', 'description', 'context']
    success_url = reverse_lazy('post:post_list')

    class Meta:
        widgets = {
            'title':forms.TextInput(),
            'description':forms.TextInput(),
            'context':forms.CharField(widget=CKEditorUploadingWidget()),
        }

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostUV(UpdateView):
    model = Post
    fields = ['title', 'description', 'context']
    success_url = reverse_lazy('post:post_list')

class PostDelV(DeleteView):
    model = Post
    success_url = reverse_lazy('post:post_list')
