from django.db import models
from apps.devtools.models import Devtool

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/%Y%m%d/', blank=True)
    content = models.TextField()
    interest = models.PositiveIntegerField(default=0)
    devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class IdeaStar(models.Model):
    session_key = models.CharField(max_length=40, default='temp-session')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('session_key', 'post')