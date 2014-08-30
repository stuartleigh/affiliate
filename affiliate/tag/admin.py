from django.contrib import admin

from .models import Tag

@admin.register(Tag)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_filter = ('site__domain',)

    prepopulated_fields = {"slug": ("title",)}