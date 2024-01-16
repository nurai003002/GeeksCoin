from django.contrib import admin

from apps.users.models import User
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'age', 'direction', 'balance', 'wallet_address')
    list_filter = ('username', 'phone', 'age', 'direction', 'balance', 'wallet_address')