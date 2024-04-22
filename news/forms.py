from django.contrib.auth.models import User
from django import forms

from .models import News, Category, Comment,MyUser


class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']


class UserForm(forms.ModelForm):
	class Meta:
		model = MyUser
		fields = ['first_name', 'last_name',  'username', 'password', 'email']


class UserEditForm(forms.ModelForm):
	class Meta:
		model = MyUser
		fields = ['first_name', 'last_name', '' 'username',  'email']

class PasswordForm(forms.Form):

	password_1 =  forms.CharField(max_length=15) 
	password_2 =  forms.CharField(max_length=15) 


class LoginForm (forms.Form):
	username = forms.CharField(max_length=200)
	password = forms.CharField(max_length=17)
	

class NewsForm(forms.ModelForm):
	class Meta:
		model = News
		fields = ['title', 'text', 'rasm', 'tur', 'author']



class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['izoh']
	
	