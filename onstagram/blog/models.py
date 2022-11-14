import datetime
from distutils.command.upload import upload

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

""" Post model """
class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.CharField(max_length=400,null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="blogpost", blank=True)
    post_image = models.ImageField(upload_to="image", null=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk":self.pk})


""" Comment model """
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments" , on_delete=models.CASCADE)
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    date_added = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return '%s - %s - %s' %(self.post.title, self.name, self.id)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={"pk":self.pk})



