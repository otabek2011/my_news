from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
	rasm = models.ImageField(default='rasm/news_photo.png')
	birthday = models.DateField(null=True, blank=True)
	

class Category(models.Model):
	name = models.CharField(max_length =50)

	def __str__(self):
		return self.name


class News(models.Model):
	title = models.CharField (max_length = 100, default='No titled news') 
	text = models.TextField()
	rasm = models.ImageField (upload_to = "rasm/", null=False, blank=True, default='news_photo.png') 
	author = models.ForeignKey(MyUser, on_delete = models.CASCADE,null=True, blank=True)
	tur = models.ForeignKey(Category, on_delete = models.CASCADE)
	created = models.DateTimeField(auto_now_add = True)
	views = models.PositiveBigIntegerField(default=0)
	likes = models.ManyToManyField(MyUser, related_name='likes')

	def __str__(self):
		return self.title

class Comment(models.Model):
	izoh = models.TextField()
	user = models.ForeignKey(MyUser,  on_delete= models.CASCADE)
	news = models.ForeignKey(News, on_delete= models.CASCADE, related_name='comments')
	created = models.DateTimeField(auto_now_add = True)  
 
	def __str__(self):
		return self.izoh[:20]
