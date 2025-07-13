import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


def get_gpt_response(messages, model="gpt-3.5-turbo", temperature=0.5):
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(str(messages))
    resp = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    return resp.choices[0].message.content
