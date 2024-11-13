from django.contrib import admin
from .models import Blog, Contact, Resume, PDFFile, Post, Item, ItemCategory,Portfolio, TeamMember
from .models import Testimonial
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'date_posted']
    search_fields = ['title', 'author']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    search_fields = ['name', 'email', 'subject']

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['file', 'description', 'uploaded_at']
    search_fields = ['description']

@admin.register(PDFFile)
class PDFFileAdmin(admin.ModelAdmin):
    list_display = ['title', 'uploaded_at']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'published_date']
    list_filter = ['category', 'is_featured']
    search_fields = ['title', 'content']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'seller', 'price', 'posted_on', 'category']
    list_filter = ['category', 'posted_on']
    search_fields = ['title', 'description']

@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']



admin.site.register(Portfolio)



@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')






admin.site.register(Testimonial)