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
        
        
        print(comment) 
        if "haHAA"in (comment.body) and comment.id not in repliedComments and not comment.author == r.user.me():
            print ("HaHAA string found: "+ comment.id)
            
            comment.reply('haHAA xD im 12 btw ;) \n\n\n\nI am a bot...beep boop | [Source code](https://github.com/joshbarbee/Reddit-bot)')
            print("replied to comment[hahaa]: "+comment.id)
            repliedComments.append(comment.id)

            with open("repliedComments.txt", "a") as f:
                f.write(comment.id + "\n")
        
            print (repliedComments)
            time.sleep(600)
            print("Sleeping...")
        elif  "lol"in (comment.body) and comment.id not in repliedComments and not comment.author == r.user.me() and len(comment.body)<4:
            print ("lol string found: "+ comment.id)
            
            comment.reply('lol? LOL???? ARE YOU TELLING ME THAT YOU FUCKING JUST LAUGHED OUT LOUD AND YOU DIDNT JUST GIVE OUT A SLIGHTLY LOUDER BREATH? THE FUCKING WORD LOL IS SO OVERUSED LIKE HEHEHE 😀LOL 😀😀LOL 😀😀LOLOL😀 HOW WOULD YOU BE IF YOU SAID SOMETHING HALAROIS AND I FUCKING JUST REPLY LOL LIKE WHAT THE FUCK. \n\n\n\nI am a bot...beep boop | [Source code](https://github.com/joshbarbee/Reddit-bot)')
            #credits to previous pasta goes to u/tk-3925
            print("replied to comment[lol]: "+comment.id)
            repliedComments.append(comment.id)

            with open("repliedComments.txt", "a") as f:
                f.write(comment.id + "\n")
        
            print (repliedComments)
            time.sleep(600)
            print("Sleeping...")
        elif "xD" in (comment.body) and comment.id not in repliedComments and not comment.author == r.user.me() and len(comment.body)<3:
            print ("xD: "+ comment.id)
            
            comment.reply('ello judge jury i am here to discuss a burning issue in our subreddit the banning of the word "xd" as we all know we have used the word constantly throughout the life time of the subreddit but that still does not mean it can get annoying and or repetitive we have used xd so much that the word lost its meaning it is for the betterment of the subredditf we banned the usege of the word "xd"\n\n\n\nI am a bot...beep boop | [Source code](https://github.com/joshbarbee/Reddit-bot)')
            #credits to previous pasta goes to u/blastgamez
            print("replied to comment[xD]: "+comment.id)
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
