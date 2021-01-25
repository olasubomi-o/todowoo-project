from django.contrib import admin
from .models import Todo

class TodoRead(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoRead)

# Register your models here.
