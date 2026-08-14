import requests
from bs4 import BeautifulSoup
import telegram

TOKEN = '8536689660:AAHpV6o7d2YfVQgWNwM7FJIl0zb9VM5SVoM'
CHAT_ID = '558200163'

def check_events():
    bot = telegram.Bot(token=TOKEN)
    url = 'https://www.digitel.tel-aviv.gov.il/'
    
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # חיפוש רחב יותר של כל הקישורים או הכותרות בדף
        items = soup.find_all(['a', 'h2', 'h3', 'span'])
        
        found_events = []
        for item in items:
            text = item.get_text(strip=True)
            # סינון טקסטים הגיוניים שיכולים להיות אירועים
            if text and len(text) > 8 and text not in found_events:
                if any(word in text for.lower() for word in ['אירוע', 'הופעה', 'סדנה', 'פסטיבל', 'ללא תשלום', 'דיגיתל']):
                    found_events.append(text)
        
        if not found_events:
            # אם לא נמצאו מילות מפתח ספציפיות, ניקח את הכותרות הראשיות הראשונות
            for item in soup.find_all(['h2', 'h3']):
                text = item.get_text(strip=True)
                if text and len(text) > 5 and text not in found_events:
                    found_events.append(text)

        if found_events:
            message = "✨ אירועים ומבצעים שעלו לדיגיתל:\n\n" + "\n".join([f"• {ev}" for ev in found_events[:5]])
        else:
            message = "הבוט סרק את אתר דיגיתל בהצלחה, אך כרגע מבנה העמוד דרש התאמה נוספת."
            
        bot.send_message(chat_id=CHAT_ID, text=message)
        
    except Exception as e:
        bot.send_message(chat_id=CHAT_ID, text=f"שגיאה בהרצת הבוט: {e}")

if __name__ == '__main__':
    check_events()
