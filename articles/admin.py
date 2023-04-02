from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter  = ('author',)
    search_fields = ('title', 'author', 'description', 'created_at')
    


admin.site.register(Article, ArticleAdmin)