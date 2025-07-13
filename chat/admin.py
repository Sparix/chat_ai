from django.contrib import admin
from .models import ChatMessage, AIPromptPreset


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'sender', 'created_at')
    list_filter = ('sender', 'created_at')
    search_fields = ('message',)
    ordering = ('-created_at',)


@admin.register(AIPromptPreset)
class AIPromptPresetAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")
    search_fields = ("name",)
