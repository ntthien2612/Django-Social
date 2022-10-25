from django.db import models
from django.contrib.auth.models import User

""" Model for User Profile """

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    date_of_birth = models.CharField(blank=True,max_length=150)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True, null=True)


    def profile_posts(self):
        return self.user.post_set.all()
    def __str__(self):
        return f'{self.user.username} Profile'

