from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework import status

from .chat_ai import process_user_message
from .models import ChatMessage, AIPromptPreset
from .serializers import ChatMessageReadSerializer, ChatMessageWriteSerializer, PromptPresetSerializer


class ChatGPTViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChatMessageReadSerializer

    def get_queryset(self):
        return ChatMessage.objects.filter(user=self.request.user).order_by("created_at")

    def get_serializer_class(self):
        if self.action == "create":
            return ChatMessageWriteSerializer
        return ChatMessageReadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)

        ai_msg = process_user_message(
            user=request.user,
            user_message=serializer.validated_data["message"],
        )

        read_serializer = ChatMessageReadSerializer(ai_msg)
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)


class AiPromptViewSet(viewsets.ModelViewSet):
    queryset = AIPromptPreset.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PromptPresetSerializer
