import site

from django.contrib import admin

from userauths.models import Profile, User


class UserAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone_number']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'gender', 'city', 'country']
    search_fields = ['full_name', 'email', 'phone_number']
    list_filter = ['date']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(User, UserAdmin)
