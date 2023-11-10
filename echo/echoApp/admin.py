from django.contrib import admin

from echoApp.models import User, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "photo")





