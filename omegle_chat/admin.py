from django.contrib import admin

# Register your models here.
from .models import User, Chat, Request


class UserAdmin(admin.ModelAdmin):
    list_display = ["MAC", "age", "sex", "hostel"]
    list_display_links = ["MAC"]
    list_filter = ["age"]
    search_fields = ["MAC", "age", "sex", "hostel"]

    class Meta:
        model = User


class ChatAdmin(admin.ModelAdmin):
    list_display = ["user1", "user2", "status"]
    list_display_links = ["user1"]
    search_fields = ["user1", "user2", "status"]

    class Meta:
        model = Chat


class RequestAdmin(admin.ModelAdmin):
    list_display = ["user1", "age", "sex", "timestamp"]
    list_display_links = ["user1"]
    search_fields = ["user1", "age", "sex"]
    list_filter = ["timestamp"]

    class Meta:
        model = Request


admin.site.register(User, UserAdmin)
admin.site.register(Chat, ChatAdmin)
admin.site.register(Request, RequestAdmin)
