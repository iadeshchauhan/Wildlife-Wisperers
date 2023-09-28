from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ExtendedUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fav_blog = models.ManyToManyField('BlogPost', related_name='favorited_by')

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')  
    upvotes = models.PositiveIntegerField(default=0)  
    likes = models.ManyToManyField(ExtendedUser, related_name='liked_posts')  
    categories = models.ManyToManyField(Category, related_name='blog_posts')  

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.SET_NULL, null=True, related_name='comments')

    def __str__(self):
        return self.content



