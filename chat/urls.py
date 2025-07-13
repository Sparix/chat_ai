from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ChatGPTViewSet, AiPromptViewSet

router = DefaultRouter()
router.register('chat', ChatGPTViewSet, basename='chat')
router.register('prompt', AiPromptViewSet, basename='prompt')

urlpatterns = [
    path('', include(router.urls)),
]
