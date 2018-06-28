from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, verbose_name='Title')
    post = models.TextField(verbose_name='Post')
    post_time = models.DateTimeField()
    update_time = models.DateTimeField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.post_time = timezone.now()
        self.update_time = timezone.now()
        return super(Post, self).save(*args, **kwargs)





