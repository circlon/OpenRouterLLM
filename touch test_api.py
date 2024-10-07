import requests
import json

# Ваш API ключ
api_key = "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"

# URL и заголовки запроса
url = "https://openrouter.ai/api/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://openrouter.ai"
}

# Данные запроса
data = {
    "model": "openai/gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are an AI assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ],
    "max_tokens": 100,
    "temperature": 0.7
}

# Отправка POST-запроса
try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()  # Проверка на ошибки HTTP
    result = response.json()
    print("Ответ от API:")
    print(json.dumps(result, indent=2))  # Форматированный вывод JSON
except requests.exceptions.RequestException as e:
    print(f"Произошла ошибка: {e}")