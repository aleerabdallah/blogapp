from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', related_name='categories')
	published_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-published_on',)

	def __str__(self):
		return self.title



class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.CharField(max_length=500)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('created_on',)

	def __str__(self):
		return f"Comment by {self.name} on {self.post}"


class Task(models.Model):
	title = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.CharField(null=True, blank=True, max_length=200)
	completed = models.BooleanField(default=False)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-created_on']


