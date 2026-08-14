import requests
from bs4 import BeautifulSoup
import telegram

TOKEN = '8536689660:AAHpV6o7d2YfVQgWNwM7FJIl0zb9VM5SVoM'
CHAT_ID = '558200163'

def check_events():
    bot = telegram.Bot(token=TOKEN)
    url = 'https://www.digitel.tel-aviv.gov.il/'
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # חיפוש כותרות של אירועים באתר דיגיתל
        events = soup.find_all(['h3', 'h2', 'a'], class_=lambda x: x and ('title' in x.lower() or 'event' in x.lower()))
        
        found_events = []
        for event in events:
            text = event.get_text(strip=True)
            if text and len(text) > 5 and text not in found_events:
                found_events.append(text)
        
        if found_events:
            message = "✨ אירועים חדשים שעלו לדיגיתל:\n\n" + "\n".join([f"• {ev}" for ev in found_events[:5]])
        else:
            message = "הבוט סרק את אתר דיגיתל, כרגע לא נמצאו כותרות חדשות או שהמבנה השתנה מעט."
            
        bot.send_message(chat_id=CHAT_ID, text=message)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check_events()
