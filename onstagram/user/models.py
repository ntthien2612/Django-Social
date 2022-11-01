from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

""" Model for User Profile """

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField("self", related_name="follow_by", symmetrical=False,blank=True)
    date_of_birth = models.CharField(blank=True,max_length=150)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='image/default.png', upload_to='image',blank=True, null=True)


    def profile_posts(self):
        return self.user.post_set.all()

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            user_profile = Profile(user=instance)
            user_profile.save()
            # user_profile.following.add(instance.profile)
            # user_profile.save()

    # def __str__(self):
    #     return f'{self.user.username} Profile'

