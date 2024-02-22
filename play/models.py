from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=100)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(null=False, unique=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	img = models.ImageField(upload_to='blog/post/images')
	description = models.CharField(max_length=200)
	body = RichTextField(blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default='', related_name='categories')
	published_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-published_on',)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('post_detail', kwargs={"slug": self.slug})
    
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs)



class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
	name = models.CharField(max_length=80)
	email = models.EmailField(default='example@gmail.com')
	body = models.CharField(max_length=500)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=False)

	class Meta:
		ordering = ('created_on',)

	def __str__(self):
		return f"Comment by {self.name} on {self.post}"


class Reply(models.Model):
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.CharField(max_length=500)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=False)

	class Meta:
		ordering = ('created_on',)
		verbose_name_plural = 'Replies'

	def __str__(self):
		return f"Reply by {self.name} on {self.comment}"



