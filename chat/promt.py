from chat.presets import get_active_presets, MAIN_LANGUAGE, FILL_DOCUMENT_PROMPT


def get_system_prompts(prompts: list | None = None):
    base_prompt = [MAIN_LANGUAGE]
    if prompts:
        base_prompt += prompts

    system_prompts = [
        {"role": "system", "content": preset}
        for preset in base_prompt + get_active_presets()
    ]
    return system_prompts
