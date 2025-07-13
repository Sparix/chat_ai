from .models import AIPromptPreset

MAIN_LANGUAGE = (
    "Always answer in the same language as the user's input."
)

FILL_DOCUMENT_PROMPT = (
    "You are an assistant for filling out documents. "
    "Answer only in valid JSON format that fills in all required fields of the document. "
    "Always use a formal, business-like, official style of language in your answers. Do not use colloquial, "
    "conversational, or slang words. Write all field values as if for an official legal document."
    "Do not add explanations, just JSON. "
    "The document fields are as follows (with descriptions): "
    "- case_name: string, required. The title of the case"
    "- case_number: string, required. The case number if available, or leave empty"
    "- service_category: string, required. The main service category chosen from predefined options,"
    "- subcategory: string, required. A free-form subcategory or leave empty"
    "- case_description: string, required, max 100 characters. Brief description of the case. "
    "Return only valid JSON with these keys. Do not include any text or explanations outside of the JSON. "
    "If a field cannot be filled from the input, leave it empty (''). "
    "Do not invent data. "
    "IMPORTANT: Use the same language as the user's input in all field values and keys."
)


def get_active_presets():
    return list(AIPromptPreset.objects.filter(is_active=True).values("prompt"))
