from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    class PostObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='answer')

    context = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='un_answer')
    object = models.Manager()  # default manager
    post_object = PostObject()  # custom manager
