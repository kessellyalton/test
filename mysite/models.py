from django.db import models
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
import bleach
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


# Blog model
class Blog(models.Model):
    title = models.CharField(max_length=200, default='Untitled')
    author = models.CharField(max_length=100, default='Anonymous')
    content = CKEditor5Field('Content')
    date_posted = models.DateTimeField(default=timezone.now, blank=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.content = bleach.clean(
            self.content,
            tags=['p', 'strong', 'em', 'a'],
            attributes={'a': ['href', 'title']},
            strip=True
        )
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', args=[self.pk])

# Contact model
class Contact(models.Model):
    name = models.CharField(max_length=100, default='John Doe')
    email = models.EmailField(default='example@example.com')
    subject = models.CharField(max_length=200, default='No Subject')
    message = models.TextField(default='No message')
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"






# Resume model
class Resume(models.Model):
    file = models.FileField(upload_to='resume/')
    description = models.CharField(max_length=255, blank=True, default='No description provided')
    uploaded_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.file.name


# PDFFile model
class PDFFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Post model with predefined categories
class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Web', 'Web'),
        ('Tech', 'Tech'),
        ('Business', 'Business'),
        ('Health', 'Health'),
        ('Opinion', 'Opinion'),
    ]

    title = models.CharField(max_length=255)
    #content = models.TextField()
    content = CKEditor5Field('ontent', config_name='default')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='press_images/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    author = models.CharField(max_length=255, blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# ItemCategory model for items in the marketplace
class ItemCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# Item model for marketplace items
class Item(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    #description = models.TextField()
    description = CKEditor5Field('Description', config_name='default')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/')
    category = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# BusinessCategory model for directory categories
class BusinessCategory(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


# Business model for directory listings
class Business(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(BusinessCategory, related_name='businesses', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    image_url = models.URLField(blank=True, null=True)
    opened_on = models.DateTimeField()
    rating = models.IntegerField(default=0)
    reviews_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name







# Portfolio model
class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('research', 'Research and Consultancy'),
        ('analytics', 'Data Analytics and Reporting'),
        ('infrastructure', 'Data Infrastructure Development'),
        ('planning', 'Strategic Planning'),
        ('stem', 'STEM Education Promotion'),
        ('training', 'Training and Capacity Building'),
        ('technology', 'Technology Import and Supply'),
        ('software', 'Customized Software Solutions'),
    ]

    title = models.CharField(max_length=200)
    description = CKEditor5Field('Description', config_name='default')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='portfolio_images/')
    client = models.CharField(max_length=100, blank=True, null=True)
    project_date = models.DateField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio-detail', args=[str(self.id)])

# TeamMember model
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    #bio = models.TextField()
    bio  = CKEditor5Field('Bio ', config_name='default')
    image = models.ImageField(upload_to='team_images/')
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
   # quote = models.TextField()
    quote = CKEditor5Field('Quote ', config_name='default')
    author_name = models.CharField(max_length=100)
    author_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name} - {self.author_title}"

