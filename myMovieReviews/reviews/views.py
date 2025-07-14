from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Review

# Create your views here.

#리뷰 리스트 보기
class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'
    context_object_name = 'reviews'

    def get_queryset(self):
        sort = self.request.GET.get('sort')
        if sort == 'rating':
            return Review.objects.all().order_by('-rating')  

        return Review.objects.all().order_by('-created_at')

#리뷰 상세보기
class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'
    context_object_name = 'review'

#리뷰작성
class ReviewCreateView(CreateView):
    model = Review
    fields = '__all__'

    
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('review_list')

#립ㅍ 수정
class ReviewUpdateView(UpdateView):
    model = Review
    fields = '__all__'
    template_name = 'reviews/review_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

#리뷰 삭제   
class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'reviews/review_confirm_delete.html'
    success_url = reverse_lazy('review_list')


 
