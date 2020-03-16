from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from Post.models import Post
from bucket.models import Bucket
from photo.models import Photo, Photolog

class pageHub(ListView):
    template_name = 'hub/main.html'
    model = Post
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        # 기본 구현을 호출해 context를 가져온다.
        context = super(pageHub, self).get_context_data(**kwargs)
        # 모든 책을 쿼리한 집합을 context 객체에 추가한다.
        context['photologs'] = Photolog.objects.all()
        context['buckets'] = Bucket.objects.all()
        return context
