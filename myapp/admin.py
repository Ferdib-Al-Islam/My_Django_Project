from django.contrib import admin
from .models import List


class listAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Description', 'image_tag')



admin.site.register(List, listAdmin)