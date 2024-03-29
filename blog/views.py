from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from . models import Post, Comment, Category
from . forms import CommentForm, RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout





def index(request):
	posts = Post.objects.all()
	context = {'posts': posts}

	return render(request, 'blog/home.html', context)

def posts(request):
	posts = Post.objects.all()
	context = {'posts': posts}

	return render(request, 'blog/posts.html', context)


def post(request, slug):
	post = Post.objects.get(slug=slug)
	comments = post.comments.filter(active=True)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			comment = Comment(post=post, name=cd['name'], email=cd['email'], body=cd['body'])
			comment.save()
			messages.add_message(request, messages.SUCCESS, "Your message is being moderated!")
			return redirect('post_detail', post.slug)
		else:
			return HttpResponse('Invalid')
	else:
		form = CommentForm()
		context = {'form': form, 'comments': comments, 'post': post}
		return render(request, 'blog/post.html', context)



def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			if cd['password'] == cd['password2']:
				new_user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
				new_user.save()
				return HttpResponse("Registered Successfully!")
			else:
				message = form.errors.as_data()
				return HttpResponse(message)
		else:
			message = form.errors.as_data()
			return HttpResponse(message)
	else:
		form = RegisterForm()
		context = {'form': form}
		return render(request, 'blog/register.html', context)


def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			try:
				user = User.objects.get(username=cd['username'])
			except:
				messages.error(request, 'User does not exist')
			user = authenticate(request, username=cd['username'], password=cd['username'])
			if user is not None:
				login(request, user)
				return redirect("todo-home")
			else:
				messages.error(request, "Username or password is incorrect")
	else:
		form = LoginForm()
		context = {'form': form}
		return render(request, 'blog/login.html', context)



def aboutUs(request):
	return render(request, 'blog/about.html')


def contactUs(request):
	return render(request, 'blog/contact_us.html')



