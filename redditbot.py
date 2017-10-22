import praw
import config
import time

def bot_login():
    print('Logging in..')
    r = praw.Reddit(username=config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "haHAA bot haHAA responder v 0.1")
    print("Logged in...")
    return r
def run_bot(r):
    for comment in r.subreddit('test').comments(limit=25):
        if "haHAA" in comment.body:
            print ("HaHAA string found"+ comment.id)
            comment.reply('haHAA xD im 12 btw ;)')
            print("replied to comment"+comment.id)
    time.sleep(10)
    print("Sleeping...")
r = bot_login()
while True:
    run_bot(r)