from openai import OpenAI

client = OpenAI(api_key="your gpt api key")

response = client.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-4", "gpt-3.5-turbo", etc.
    messages=[
        {"role": "system", "content": "You are a vietual assistant named jarvis skilled in general tasks like alexa and google"},
        {"role": "user", "content": "what is coding"}
    ]
)

print(response.choices[0].message)
