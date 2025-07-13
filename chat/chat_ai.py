import json

from .models import ChatMessage
from .presets import FILL_DOCUMENT_PROMPT
from .promt import get_system_prompts
from .ai_connection import get_gpt_response


# def process_user_message(user, user_message):
#     ChatMessage.objects.create(message=user_message, sender="user", user=user)
#
#     history = list(ChatMessage.objects.filter(user=user).order_by('-created_at')[:50][::-1])
#     prompts = []
#     fill_document = False
#     if user_message.startswith("/fill_document"):
#         fill_document = True
#         prompts.append(FILL_DOCUMENT_PROMPT)
#
#     system_prompts = get_system_prompts(prompts)
#     messages = [*system_prompts]
#     for msg in history:
#         messages.append({
#             "role": "user" if msg.sender == "user" else "assistant",
#             "content": msg.message
#         })
#     messages.append({"role": "user", "content": user_message})
#     bot_text = get_gpt_response(messages)
#
#     if fill_document:
#         bot_text = json.loads(bot_text)
#
#     ai_msg = ChatMessage.objects.create(message=bot_text, sender="ai", user=user)
#
#     return ai_msg


def process_user_message(user, user_message):
    ChatMessage.objects.create(message=user_message, sender="user", user=user)
    history = list(ChatMessage.objects.filter(user=user).order_by('-created_at')[:0][::-1])

    if user_message.startswith("/"):
        ai_msg = handle_special_command(user, user_message, history)
    else:
        ai_msg = handle_regular_message(user, user_message, history)
    return ai_msg


def handle_special_command(user, user_message, history):
    if user_message.startswith("/fill_document"):
        prompts = [FILL_DOCUMENT_PROMPT]
        system_prompts = get_system_prompts(prompts)
        messages = [*system_prompts]
        for msg in history:
            messages.append({
                "role": "user" if msg.sender == "user" else "assistant",
                "content": msg.message
            })
        messages.append({"role": "user", "content": user_message})
        bot_text = get_gpt_response(messages)
        bot_data = json.loads(bot_text)

        ai_msg = ChatMessage.objects.create(message=bot_text, sender="ai", user=user, properties=bot_data)
        return ai_msg
    raise NotImplementedError("Unknown command!")


def handle_regular_message(user, user_message, history):
    system_prompts = get_system_prompts([])
    messages = [*system_prompts]
    for msg in history:
        messages.append({
            "role": "user" if msg.sender == "user" else "assistant",
            "content": msg.message
        })
    messages.append({"role": "user", "content": user_message})
    bot_text = get_gpt_response(messages)
    ai_msg = ChatMessage.objects.create(message=bot_text, sender="ai", user=user)
    return ai_msg
