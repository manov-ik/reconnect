from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    phone_no = models.CharField(max_length=15, unique=True)
    roll_no = models.CharField(max_length=20, unique=True)
    dept = models.CharField(max_length=100)
    interests = models.ForeignKey("Interest", on_delete=models.SET_NULL, null=True, blank=True)

    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)  # ✅ Fixed
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)  # ✅ Fixed

    def __str__(self):
        return self.username

class Interest(models.Model):
    # name = models.CharField(max_length=100, unique=True)  # Interest category name (e.g., AI, Robotics, etc.)
    field1 = models.CharField(max_length=100, blank=True, null=True)
    field2 = models.CharField(max_length=100, blank=True, null=True)
    field3 = models.CharField(max_length=100, blank=True, null=True)
    field4 = models.CharField(max_length=100, blank=True, null=True)
    field5 = models.CharField(max_length=100, blank=True, null=True)
    roll_no = models.CharField(max_length=20, unique=True)
    def __str__(self):
        return self.roll_no

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Unique group name
    description = models.TextField(blank=True, null=True)  # Group description
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when group was created

    def __str__(self):
        return self.name

class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)  # Which group
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Which user
    role = models.CharField(max_length=50, choices=[("admin", "Admin"), ("member", "Member")])  # User role
    joined_at = models.DateTimeField(auto_now_add=True)  # When user joined

    def __str__(self):
        return f"{self.user.username} in {self.group.name}"

class DirectMessage(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="received_messages")
    content = models.TextField()
    status = models.CharField(max_length=10, choices=[("sent", "Sent"), ("delivered", "Delivered"), ("read", "Read")], default="sent")
    media_url = models.URLField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"DM from {self.sender.username} to {self.receiver.username}"

class GroupMessage(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Who sent the message
    group = models.ForeignKey(Group, on_delete=models.CASCADE)  # Which group
    content = models.TextField()  # Message text
    media_url = models.URLField(blank=True, null=True)  # Image/Video link
    timestamp = models.DateTimeField(auto_now_add=True)  # When message was sent

    def __str__(self):
        return f"Group message in {self.group.name} by {self.sender.username}"

class Event(models.Model):
    name = models.CharField(max_length=255)  # Event name
    media_url = models.URLField(blank=True, null=True)  # Event media (image/video)
    description = models.TextField()  # Event description
    reg_link = models.URLField()  # Registration link
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Who created the event
    created_at = models.DateTimeField(auto_now_add=True)  # Event creation date

    def __str__(self):
        return self.name
