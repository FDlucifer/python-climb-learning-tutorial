# pip install openai

import openai

openai.api_key = ""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "do you have a mother?"}
    ]
)

print(response)