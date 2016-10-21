from __future__ import unicode_literals

from django.db import models
from ..user_app.models import User

# Create your models here.
class Author(models.Model):
    author = models.CharField(max_length=30)
    user=models.ForeignKey('user_app.User',related_name="reviews_author")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.TextField()
    author=models.ManyToManyField(Author,related_name="books_author")
    user=models.ForeignKey('user_app.User',related_name="books_user")
    # user = models.ForeignKey(User,related_name="secrets")
    # liker = models.ManyToManyField('user_app.User',related_name="secret_user")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Review(models.Model):
    review = models.TextField()
    user=models.ForeignKey('user_app.User',related_name="reviews_user")
    book = models.ForeignKey(Book,related_name="reviews")
    # user = models.ForeignKey(User,related_name="secrets")
    # liker = models.ManyToManyField('user_app.User',related_name="secret_user")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
