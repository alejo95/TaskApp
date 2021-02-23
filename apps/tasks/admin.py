from django.contrib import admin
from apps.tasks.models import *

class CategoryTaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(CategoryTask, CategoryTaskAdmin)
admin.site.register(Tasks)
