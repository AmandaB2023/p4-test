from django.contrib import admin
from .models import About
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)

class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)