from django.contrib import admin
from .models import CustomUser, Interest, Group, GroupUser, DirectMessage, GroupMessage, Event

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Interest)
admin.site.register(Group)
admin.site.register(GroupUser)
admin.site.register(DirectMessage)
admin.site.register(GroupMessage)
admin.site.register(Event)