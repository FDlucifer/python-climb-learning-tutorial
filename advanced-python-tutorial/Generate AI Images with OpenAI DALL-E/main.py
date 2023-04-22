# pip install openai

import openai

openai.api_key = "sk-jkjasdckasdnjAoEpsHHw"

response = openai.Image.create(
  prompt="rainbow in the rain",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)
