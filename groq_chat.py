import os
from groq import Groq
from dotenv import load_dotenv
import pprint

load_dotenv()
client = Groq(
    api_key=os.getenv('GROQ_API_KEY')
)

pergunta = input('Faca a pergunta: ')

chat = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": pergunta
        }
    ],
    model="llama-3.3-70b-versatile"
)
pprint.pp(chat.choices[0].message.content)