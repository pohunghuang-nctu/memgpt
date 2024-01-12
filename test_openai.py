from openai import OpenAI
import openai

openai.api_key = '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'

client = OpenAI(api_key=openai.api_key)

response = client.chat.completions.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

print(response.choices[0].message.content)