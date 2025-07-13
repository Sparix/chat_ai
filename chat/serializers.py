from rest_framework import serializers
from .models import ChatMessage, AIPromptPreset


class ChatMessageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ("id", "user", "message", "properties", "sender", "created_at")
        read_only_fields = fields


class ChatMessageWriteSerializer(serializers.Serializer):
    message = serializers.CharField()


class PromptPresetSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = AIPromptPreset
        fields = (
            "id",
            "name",
            "prompt",
            "description",
            "is_active",
            "created_at",
        )
