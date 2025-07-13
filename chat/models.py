from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ChatMessage(models.Model):
    SENDER_CHOICES = [
        ('user', 'User'),
        ('ai', 'AI'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_messages')
    message = models.TextField()
    properties = models.JSONField(blank=True, default={}) #
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES, default='user')


class AIPromptPreset(models.Model):
    name = models.CharField(max_length=100, unique=True)
    prompt = models.TextField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
