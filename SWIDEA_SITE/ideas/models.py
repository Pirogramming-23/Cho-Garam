from django.db import models

class Idea(models.Model):
    DEVTOOL_CHOICES = [
        ('VSCode', 'VSCode'),
        ('PyCharm', 'PyCharm'),
        ('IntelliJ', 'IntelliJ'),
        ('Eclipse', 'Eclipse'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=32)
    user = models.CharField(max_length=32)
    image = models.ImageField(upload_to='idea_images/', blank=True, null=True)
    content = models.TextField()
    interest = models.IntegerField(default=0)
    devtool = models.CharField(max_length=20, choices=DEVTOOL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
