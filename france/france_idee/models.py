from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField

# Create your models here.

class Hopital(models.Model):
    titre = models.CharField(max_length=250)
    auteur = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    description = FroalaField()
    likes = models.ManyToManyField(User, related_name='like_post')


class Scolaire(models.Model):
    titre = models.CharField(max_length=250)
    auteur = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    description = FroalaField()
    likes = models.ManyToManyField(User, related_name='like_posts')


class Agriculture(models.Model):
    titre = models.CharField(max_length=250)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    description = FroalaField()
    likes = models.ManyToManyField(User, related_name='like_posta')

