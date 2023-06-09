from django.contrib import admin

from .models import Category, Comment, Genre, Review, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'pub_date', 'author', 'review')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


class TitleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'description', 'category')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'author', 'score', 'pub_date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
