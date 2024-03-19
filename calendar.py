from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime
import os 

# Scopes für den Zugriff auf den Kalender festlegen
SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_credentials():
    creds = None
    # Die Datei, in der die Zugriffsberechtigungen gespeichert werden. Sollte nach dem ersten Durchlauf vorhanden sein.
    token_path = 'token.json'

    # Überprüfen, ob bereits Zugriffsberechtigungen gespeichert wurden
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path)
    # Wenn keine Zugriffsberechtigungen verfügbar sind, die Authentifizierungsprozess durchlaufen
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Zugriffsberechtigungen speichern, um zukünftige Anfragen zu autorisieren
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    return creds

def create_event():
    # Holen der Zugriffsberechtigungen
    credentials = get_credentials()
    service = build('calendar', 'v3', credentials=credentials)

    # Datum und Uhrzeit für den Ereignisstart festlegen
    start_time = datetime.datetime.now()
    end_time = start_time + datetime.timedelta(hours=1)

    # Ereignisdetails festlegen
    event = {
        'summary': 'Testtermin',
        'location': 'Ort',
        'description': 'Beschreibung des Termins',
        'start': {
            'dateTime': start_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'Europe/Berlin',  # Zeitzone anpassen
        },
        'end': {
            'dateTime': end_time.strftime('%Y-%m-%dT%H:%M:%S'),
            'timeZone': 'Europe/Berlin',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},  # Eine E-Mail-Benachrichtigung 24 Stunden vor dem Termin
                {'method': 'popup', 'minutes': 10},       # Eine Popup-Benachrichtigung 10 Minuten vor dem Termin
            ],
        },
    }

    # Ereignis erstellen
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Ereignis erstellt: %s' % (event.get('htmlLink')))
