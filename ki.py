import openai
import pyttsx3

# Setzen Sie Ihren API-Schlüssel hier ein
api_key = 'YOUR_GPT_KEY'

# Einleitungstext für die Konversation
conversation_history = "Das ist ein Beispiel für eine kurze Konversation mit GPT-3."

# Initialisieren der OpenAI-API mit dem API-Schlüssel
openai.api_key = api_key

# Funktion für die Interaktion mit GPT-3
def ask_gpt3(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Verwenden Sie das GPT-3.5 Turbo-Modell
        messages=[
            {"role": "system", "content": conversation_history},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def process_input(text):
    if "jarvis" in text.lower():
        # Gib den erkannten Text aus
        print("Du hast gesagt:", text)
        response = ask_gpt3(text)
        print(f"GPT-3: {response}")
        speak_text(response)
    else:
        print("Ich reagiere nur, wenn du 'jarvis' sagst.")

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
