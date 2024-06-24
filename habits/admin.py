from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'creator', 'name', 'time', 'is_public', 'is_pleasant', 'last_reminded', )
    list_filter = ('id', 'creator', 'name', 'time', 'is_public', 'is_pleasant', 'last_reminded', )
    search_fields = ('id', 'creator', 'name', 'time', 'is_public', 'is_pleasant', 'last_reminded', )
