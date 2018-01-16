from twilio.rest import Client
import keys
import random
import schedule
import time

# Your Account SID from twilio.com/console
account_sid = "AC3a708cd623b9a48d8fa8fef632309eef"
# Your Auth Token from twilio.com/console
auth_token  = keys.token

quotes = ['We are what we repeatedly do. Excellence is not an act, but a habit.', 
'When you want something, all the universe conspires in helping you achieve it.',
'Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.',
'If you are not willing to learn no one can help you; if you are determined to learn no one can stop you.',
'If you want to go fast, go alone; if you want to arrive, go together.',
'Be who you needed when you were younger.',
'Until the lions have their historians, the story of the hunt will glorify the hunter.',
'Perseverance is the virtue of the less brilliant',
'Rise & Grind :)',
'Good morning. Imagine how you want to feel at the end of the day. Start working towards that now. Have a good breakfast tho  -Lin-Manuel Miranda',
'You have a bigger impact on the world than you think.',
'We will win.'
]

client = Client(account_sid, auth_token)

def job():
	message = client.messages.create(
    to=keys.myNumber, 
    from_="+12013807407",
    body=random.choice(quotes))
	print(message.sid)


schedule.every().day.at("9:00").do(job)

while True:
	schedule.run_pending()
	time.sleep(1)