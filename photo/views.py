from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Photo

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
