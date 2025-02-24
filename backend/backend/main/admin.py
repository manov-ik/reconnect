from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Interest, Group, GroupUser, DirectMessage, GroupMessage, Event

class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "phone_no", "roll_no", "dept")
    search_fields = ("username", "email", "roll_no", "phone_no")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("phone_no", "roll_no", "dept", "interests")}),
    )

class InterestAdmin(admin.ModelAdmin):
    list_display = ("roll_no", "field1", "field2", "field3", "field4", "field5")  
    search_fields = ("roll_no", "field1", "field2", "field3", "field4", "field5")

class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created_at")
    search_fields = ("name",)

class GroupUserAdmin(admin.ModelAdmin):
    list_display = ("user", "group", "role", "joined_at")
    list_filter = ("role", "group")
    search_fields = ("user__username", "group__name")

class DirectMessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "receiver", "content", "status", "timestamp")
    list_filter = ("status",)
    search_fields = ("sender__username", "receiver__username", "content")

class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "group", "content", "timestamp")
    search_fields = ("sender__username", "group__name", "content")

class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "posted_by", "reg_link", "created_at")
    search_fields = ("name", "posted_by__username")

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(GroupUser, GroupUserAdmin)
admin.site.register(DirectMessage, DirectMessageAdmin)
admin.site.register(GroupMessage, GroupMessageAdmin)
admin.site.register(Event, EventAdmin)

