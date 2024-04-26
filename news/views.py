from django.shortcuts import render, redirect

from .forms import NewsForm, CategoryForm, CommentForm, UserForm , LoginForm , UserEditForm , PasswordForm
from .models import *
from django.contrib.auth import authenticate, login, logout 

from django.contrib import messages


def Logout(request):
	logout(request)
	messages.info(request,'siz muvaffaqiyatlo log out bo\'ldiz')
	return redirect ("home")




	

def home(request):
	all_news = News.objects.all()
	if request.POST:
		news_id = request.POST['one']
		one_news = News.objects.get(id=news_id)

		if request.user in one_news.likes.all():
			one_news.likes.remove(request.user)
		else:
			one_news.likes.add(request.user)



 
	return render(request, 'index.html', {'all_news' : all_news })




def detail (request, id):
	a = News.objects.get(id = id)
	
	form=CommentForm()

	if request.POST:
		form=CommentForm(request.POST)
		if form.is_valid():
			Comment.objects.create(
				izoh=form.cleaned_data["izoh"],
				user=request.user,
				news=a
				)
			return redirect('detail',a.id)
	return render(request,'detail.html',{'one':a, 'form':form})	
	

def createCategory(request):
	form = CategoryForm()

	if request.POST:
		form = CategoryForm(request.POST)
		if form.is_valid():
			category = form.save()
			name = Category.name
			messages.info(request, f'siz muvaffaqiyatlo "{name}" bolimini yaratdiz ! ')
		return redirect('home')
	return render(request, 'create_category.html', {'form': form})


def user_register(request):
	form = UserForm()

	if request.POST:
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			parol = form.cleaned_data['password']
			user.set_password(parol)
			user.save()
			return redirect('home')
	return render(request, 'register.html', {'form': form})

def user_edit(request):
	form = UserEditForm(instance=request.user)
	if request.POST:
		form = UserEditForm(request.POST,instance=request.user)
		if form.is_valid():
			form.save()

			return redirect('home')
	return render (request,'register.html',{'form':form})

def password_edit(request):
	form = PasswordForm()
	if request.POST:
		form = PasswordForm(request.POST)
		p_1 = form.data['password_1']
		p_2 = form.data['password_2']
		user = request.user
		if user.check_password(p_1):
			user.set_password(p_2)
			user.save()
			return redirect('home')

	return render(request,'register.html',{'form':form})		

def createNews(request):
	form = NewsForm()

	if request.POST:
		form = NewsForm(request.POST, files=request.FILES)
		if form.is_valid():
			News.objects.create(
			# author = request.user,
			title = form.cleaned_data['title'],
			text = form.cleaned_data['text'],
			tur= form.cleaned_data['tur'],
			rasm = form.cleaned_data['rasm']
				)
			return redirect('home')
	return render(request, 'create_news.html', {'form': form})


def detail_coment(request, id , one):

	comment = Comment.objects.get(id=id)
	comment.delete()

	return redirect("delete",one)




def createComment(request, id):
	news = News.objects.get(id=id)
	form = CommentForm()

	if request.POST:
		form = CommentForm(request.POST)
		if form.is_valid():
			Comment.objects.create(
				izoh = form.cleaned_data['izoh'],
				user = request.user,
				news = news
				)
			return redirect('detail', news.id)

	return render(request, 'detail.html',{'form': form})


def edit(request,id):
	edit_news = News.objects.get(id=id)
	if request.POST:
		edit_news.title = request.POST['title']
		edit_news.text = request.POST['text']
		edit_news.rasm = request.POST['rasm']
		edit_news.save()

		return redirect('home')
	return render(request, 'edit.html', {'one_edit_news':edit_news})


def delete(request,id):
	News.objects.get(id=id).delete()
	return redirect('home')



def Login(request):
	login_form = LoginForm()
	if request.POST:
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			
			username = login_form.cleaned_data['username']
			password = login_form.cleaned_data['password']
			aaa = authenticate(request,username=username,password=password)
			if aaa is not None:
				
				print (request.user)

				login(request,aaa)

				messages.success(request, f"siz , {aaa.username}, login gilindiz ! ")

				print (request.user)

				return redirect("home")
		messages.success(request, f"username yoki parol topilmadi ! ")			
	return render(request,'login.html', {'form': login_form})




def form_edit(request,id):
	edit_news = News.objects.get(id=id)
	form = NewsForm(instance=edit_news)
	if request.POST:
		form = NewsForm(request.POST, files=request.FILES, instance=edit_news)
		if form.is_valid():
			form.save()
			return redirect('detail', edit_news.id)
	return render(request, 'form_edit.html', {'form': form})

