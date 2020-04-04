from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Photo, Photolog
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Create your views here.
class PhotoLV(ListView):
    template_name = 'photo/photo_list.html'
    model = Photo
    context_object_name = 'photos'

    def get_context_data(self, **kwargs):
        # 기본 구현을 호출해 context를 가져온다.
        context = super(PhotoLV, self).get_context_data(**kwargs)
        # 모든 책을 쿼리한 집합을 context 객체에 추가한다.
        context['range'] = range(7)
        return context

class PhotoDV(DetailView):
    template_name = 'photo/photo_detail.html'
    model = Photo

class PhotologLV(ListView):
    template_name = 'photolog_list.html'
    model = Photolog
    context_object_name = 'photologs'

class PhotologDV(DetailView):
    template_name = 'photo/photolog_detail.html'
    model = Photolog

class PhotologCV(CreateView):
    model = Photolog
    template_name = 'photo/photolog_form.html'
    fields = ['name', 'description', 'content']
    success_url = reverse_lazy('photo:photolog_list')

    class Meta:
        widgets = {
            'name':forms.TextInput(),
            'description':forms.TextInput(),
            'content':forms.CharField(widget=CKEditorUploadingWidget()),
        }

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
