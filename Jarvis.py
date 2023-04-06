import openai
import speech_recognition as sr
import pyttsx3
import time

# Biblioteca GPT-3 e Chave API
openai.api_key = #SUA API KEY da OpenAi- SEM ISSO NÃO FUNCIONA! 

# Inicializa o reconhecimento de voz
r = sr.Recognizer()

# Inicializa a engine de sintese de voz
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Define a função de reconhecimento de voz
def listen_for_command():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Diga algo")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language="pt-BR")
        return command
    except sr.UnknownValueError:
        print("Não entendi")
        return ""
    except sr.RequestError as e:
        print("Erro; {0}".format(e))
        return ""

while True:
    command = listen_for_command()
    question = command
    # Adiciona validação para garantir que o comando reconhecido é válido
    if len(question) < 1:
        continue
    # Chama a API do GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=100,
        temperature=0.5
    )
    answer = response["choices"][0]["text"]
    engine.say(answer)
    engine.runAndWait()
    print(answer)