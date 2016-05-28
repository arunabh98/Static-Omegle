from django.contrib import admin

# Register your models here.
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ["MAC", "age", "sex", "hostel"]
    list_display_links = ["MAC"]
    list_filter = ["age"]
    search_fields = ["MAC", "age", "sex", "hostel"]

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
