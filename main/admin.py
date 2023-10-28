from django.contrib import admin
from .models import Todo
# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    model = Todo
    list_display = ["datetime", "user", "done"]