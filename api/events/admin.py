from django.contrib import admin
from .models import Event, Category, Seat, Comment


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'begins_time', 'begins_date', 'category', 'has_bonuses', 'is_active', 'city',
                    'address']
    list_filter = ['begins_time', 'begins_date', 'category__name', 'has_bonuses', 'is_active', 'city', 'address']
    ordering = ['begins_date', 'begins_time']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class SeatAdmin(admin.ModelAdmin):
    list_display = ['name', 'count', 'price', 'event']
    list_filter = ['event__id']
    ordering = ['price']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'author']
    list_filter = ['author']


# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(Comment, CommentAdmin)
