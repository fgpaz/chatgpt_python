import openai
import os
from dotenv import load_dotenv


openai.api_key = os.environ.get('chat_gpt')

while True:
    
    prompt = input("\n\n------------------\nIntroduce una pregunta:\n")
    
    if prompt == "exit":
        break
    
    completion = openai.Completion.create(engine="text-davinci-003",
                                        prompt=prompt,
                                        n=1,
                                        max_tokens=2048)
    print('Respuesta:\n')
    print(completion.choices[0].text)