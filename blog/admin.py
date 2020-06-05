from django.contrib import admin
from blog.models import Banner, Category, Tag, Tui, Article, Link

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'create_time') # 要显示的字段
    list_per_page = 50 # 满50条分页
    ordering = ('-create_time',)   # 排序
    list_display_links = ('id', 'title')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','link_url')