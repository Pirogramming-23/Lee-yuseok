from django.db import models
from django.urls import reverse


# Create your models here.
class Review(models.Model):
    GENRE_CHOICES = [
        ('액션', '액션'),
        ('코미디', '코미디'),
        ('드라마', '드라마'),
        ('호러', '호러'),
        ('로맨스', '로맨스'),
        ('SF', 'SF'),
    ]

    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(
        max_length=50,
        choices=GENRE_CHOICES
        )
    rating = models.IntegerField()
    runtime = models.IntegerField()
    content = models.TextField()
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def get_absolute_url(self):
        return reverse('review_detail', args=[str(self.id)])
    
    def get_runtime_display(self):
        hours = self.runtime // 60
        minutes = self.runtime % 60
        return f"{hours}시간 {minutes}분"

