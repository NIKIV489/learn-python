'''Fake News Detector (Rule-Based)
Input: news headline
Check for clickbait patterns (“shocking”, “you won’t believe”)
Flag as suspicious'''

news = input("Enter news: ").lower()

if "shocking" in news or "you won't believe" in news:
    print("Suspicious")
else:
    print("Not suspicious")

'''
Notification System
Send notification based on:
Time
User activity
Prioritys
'''



from datetime import datetime

def notify(user_active, priority):
    hour = datetime.now().hour

    if priority == "high":
        print("Urgent notification")
    elif not user_active:
        print("User inactive reminder")
    elif 8 <= hour <= 10:
        print("Morning notification")
    else:
        print("No notification")

notify(False, "medium")
