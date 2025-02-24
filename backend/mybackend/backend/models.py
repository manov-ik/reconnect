from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class CustomUser(AbstractUser):
    phone_no = models.CharField(max_length=15, blank=True, null=True)
    roll_no = models.CharField(max_length=20, unique=True)
    dept = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    interest = models.ForeignKey(
        'Interest', on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )

    # Fix reverse accessor clashes
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_users",  # Avoids clash with default User.groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_users_permissions",  # Avoids clash with default User.user_permissions
        blank=True
    )

    def __str__(self):
        return self.username
    
# Interest Model (One-to-One with CustomUser)
class Interest(models.Model):
    field1 = models.CharField(max_length=100, blank=True, null=True)
    field2 = models.CharField(max_length=100, blank=True, null=True)
    field3 = models.CharField(max_length=100, blank=True, null=True)
    field4 = models.CharField(max_length=100, blank=True, null=True)
    field5 = models.CharField(max_length=100, blank=True, null=True)
    roll_no = models.CharField(max_length=20, unique=True)  # Ensures every roll_no has unique interests

    def __str__(self):
        return f"Interest of {self.roll_no}"

# Group Model
class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Optional field

    def __str__(self):
        return self.name

# GroupUser Model: links a group and a user with extra info
class GroupUser(models.Model):
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE, 
        related_name='group_users'
    )
    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='group_memberships'
    )
    role = models.CharField(max_length=50)  # e.g., admin, member, moderator; you can later convert this to a choices field
    join_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('group', 'user')

    def __str__(self):
        return f"{self.user.roll_no} in {self.group.name} as {self.role}"

# DirectMessage Model: for one-to-one messaging between users
class DirectMessage(models.Model):
    sender = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='sent_direct_messages'
    )
    receiver = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='received_direct_messages'
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.CharField(max_length=20)  # e.g., 'sent', 'delivered', 'read'
    media_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Msg from {self.sender.roll_no} to {self.receiver.roll_no} at {self.timestamp}"

# GroupMessage Model: for messages sent in a group
class GroupMessage(models.Model):
    group = models.ForeignKey(
        Group, 
        on_delete=models.CASCADE, 
        related_name='messages'
    )
    sender = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        related_name='sent_group_messages'
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    media_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Group Msg in {self.group.name} by {self.sender.roll_no} at {self.timestamp}"

class Event(models.Model):
    name = models.CharField(max_length=255)  # Event name
    media_url = models.URLField(blank=True, null=True)  # Image/Video link
    description = models.TextField()  # Event description
    reg_link = models.URLField()  # Registration link
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Who created the event
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when event was created

    def __str__(self):
        return self.name  # Display event name in admin panel
