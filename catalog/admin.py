from django.contrib import admin

from catalog.models import Book, Category, Favorites, Comment

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('owner', 'book')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('book', 'commenter', 'date')
