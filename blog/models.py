from django.db import models
from django.conf import settings    
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
		)
	title = models.CharField(max_length=100)
	body = RichTextField(blank=True, null=True)
	published = models.DateTimeField(default=timezone.now, auto_now_add=True)
	image = models.ImageField(upload_to='posts')
	slug = models.SlugField(max_length=150, unique=True)
	status = models.CharField(choices=STATUS_CHOICES, max_length=50, default='draft')
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	published = models.DateTimeField(auto_now_add=True) # default=timezone.now,
	category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.SET_NULL, null=True)
	draft = models.BooleanField('Черновик', default=False)
	tags = models.ManyToManyField('Tag', related_name="post")

	class Meta:
		ordering = ('-published',)

	def __str__(self):
		return self.title + '|' + str(self.author)

	def get_absolute_url(self):
		return reverse("post_single", kwargs={"slug": self.category.url, "post_slug": self.slug})

	def get_absolute_url(self):
		return reverse('home')

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	text = models.CharField(max_length=500)
	published = models.DateTimeField(auto_now_add=True)  # default=timezone.now
	active = models.BooleanField(default=True)
	email = models.EmailField(max_length=254)

	#def __str__(self):
	#	return '%s-%s' % (self.post.title, self.name)

	class Meta:
		ordering = ('-published',)


class Category(models.Model):
	name = models.CharField(max_length=50)
	url = models.SlugField(max_length=50, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('home')


class Tag(models.Model):
	name = models.CharField(max_length=50)
	url = models.SlugField(max_length=50, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('tag', kwargs={"slug": self.url})  # url - > slug!!

	class Meta:
		ordering = ['name']