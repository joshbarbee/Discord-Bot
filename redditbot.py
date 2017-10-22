import praw
import config
import time
import os

def bot_login():
    print('Logging in..')
    r = praw.Reddit(username=config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "haHAA bot haHAA responder v 0.2")
    print("Logged in...")
    return r
def run_bot(r,repliedComments):
    
    for comment in r.subreddit('all').stream.comments():
        badsubbreddits = ["ice_posideon", 'askreddit', 'iama']
        hahaaforms = str(["hahaa", "haHaa", 'hahAA', 'HaHAa', "hAhAh", "haHAA", "HaHaa", 'HahaA'])
        print(comment) 
        if hahaaforms in (comment.body) and comment.id not in repliedComments and not comment.author == r.user.me() and len(comment.body)<10 and subreddit not in badsubbreddits:
            print ("HaHAA string found: "+ comment.id)
            
            comment.reply('haHAA xD im 12 btw ;) \n\n\n\nI am a bot...beep boop | [Source code](https://github.com/joshbarbee/Reddit-bot)')
            print("replied to comment: "+comment.id)
            repliedComments.append(comment.id)

            with open("repliedComments.txt", "a") as f:
                f.write(comment.id + "\n")
        
            print (repliedComments)
            time.sleep(600)
            print("Sleeping...")


def savedComments():
    if not os.path.isfile("repliedComments.txt"):
        repliedComments = []
    else:
        with open("repliedComments.txt", "r") as f:
            repliedComments = f.read()
            repliedComments = repliedComments.split("\r")
            repliedComments = list(filter(None, repliedComments))

    return repliedComments



r = bot_login()
repliedComments = savedComments()

while True:
    run_bot(r, repliedComments)
print (repliedComments)
