import requests
from bs4 import BeautifulSoup
import telegram

# הטוקן וזהות הצ'אט שלך מוכנים כאן בקוד כדי לחסוך לך הגדרות בענן
TOKEN = '8536689660:AAHpV6o7d2YfVQgWNwM7FJIl0zb9VM5SVoM'
CHAT_ID = '8536689660'  # נעדכן בהמשך או שנשלח הודעה ראשונה לבדיקה

def check_events():
    bot = telegram.Bot(token=TOKEN)
    url = 'https://www.digitel.tel-aviv.gov.il/'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # שליחת הודעת בדיקה ראשונית לטלגרם שלך
        # bot.send_message(chat_id=CHAT_ID, text="הבוט של דיגיתל מחובר ועובד!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check_events()
