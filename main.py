import speech_recognition as sr
from ki import process_input
from wetter import get_weather_info
from music import play_music
from system import system_stats, speak
from news import get_news, print_news


# Erstelle ein SpeechRecognition-Recognizer-Objekt
recognizer = sr.Recognizer()

# Öffne ein Mikrofon und starte dauerhafte Erkennung
with sr.Microphone() as source:
    print("Starte dauerhafte Spracherkennung...")
    while True:
        try:
            # Warte auf eine Spracheingabe
            audio = recognizer.listen(source)
            
            # Verwende die recognize_google-Methode, um Sprache in Text umzuwandeln
            text = recognizer.recognize_google(audio, language='de-DE')
                        
            # Überprüfe die erkannten Befehle und führe entsprechende Aktionen aus
            if "wetter" in text.lower():
                # Extrahiere den Stadtnamen aus dem erkannten Text
                city_name = text.split("in")[-1].strip()
                # Rufe die Funktion aus wetter.py auf, um Wetterinformationen zu erhalten
                get_weather_info(city_name)

            elif "musik" in text.lower() or "spiele" in text.lower():
                # Rufe die Funktion aus music.py auf, um Musik abzuspielen
                play_music()

            elif "email" in text.lower():
                # Hier könnte die Logik zum Senden von E-Mails implementiert werden
                pass

            elif "kalender" in text.lower():
                # Hier könnte die Logik zur Verwaltung des Kalenders implementiert werden
                pass

            elif "suche" in text.lower():
                # Hier könnte die Logik für die Internetsuche implementiert werden
                pass

            elif "system" in text.lower():
                # Rufe die Funktion system_stats() auf, um die Systemstatistiken zu lesen
                stats_text = system_stats()
                print(stats_text)
                speak(stats_text)

            elif "news" in text.lower() or "nachrichten" in text.lower():
                # Rufe die Funktion aus news.py auf, um die neuesten Nachrichten abzurufen und vorzulesen
                articles = get_news()
                print_news(articles)


            else:
                # Verarbeite den erkannten Text mit der Funktion in ki.py
                process_input(text)

        except sr.UnknownValueError:
            print("Konnte die Sprache nicht verstehen")
        except sr.RequestError as e:
            print("Fehler bei der Anfrage an die Spracherkennungs-API; {0}".format(e))
        except KeyboardInterrupt:
            print("Dauerhafte Spracherkennung gestoppt.")
            break
