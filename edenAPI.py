import json
import requests
import openai

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZWIyZGZlZmMtYmQwOC00YTkzLTllMDgtNGY4YTAwNDUxNzM3IiwidHlwZSI6ImFwaV90b2tlbiJ9.9JpqYikskkqbkuzzpaJDXMtzla78_5KMyt8zAIBLS4E"}

url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "Hello i need your help ! ",
    "chatbot_global_action": "Act as an assistant",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "Harsha"
}


def talkToAi(query):
    payload['text'] = query
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    return result['openai']['generated_text']