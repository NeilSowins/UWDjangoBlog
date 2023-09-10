from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.


class CategoriesInline(admin.TabularInline):
    model = Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoriesInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("posts",)
