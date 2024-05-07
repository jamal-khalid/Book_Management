from django.contrib import admin
from .models import Book , CustomUser , ReadingList , ReadingListEntry
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Book)
# admin.site.register(CustomUser , UserAdmin)
admin.site.register(ReadingList)
admin.site.register(ReadingListEntry)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_active']

