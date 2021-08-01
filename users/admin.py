from django.contrib import admin

from users.models import UserProfile
from api.models import Category, Genre, Title


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'first_name', 'last_name', 'username',
        'bio', 'email', 'role', 'user_code'
    )


models = [Category, Genre, Title]
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(models)
