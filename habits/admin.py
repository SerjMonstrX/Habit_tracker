from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('creator', 'name', 'time', 'is_public', 'is_pleasant', )
    list_filter = ('creator', 'name', 'time', 'is_public', 'is_pleasant', )
    search_fields = ('creator', 'name', 'time', 'is_public', 'is_pleasant', )
