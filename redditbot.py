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
        if "haHAA"in (comment.body) and comment.id not in repliedComments and not str(comment.author) == r.user.me():
            print ("HaHAA string found: "+ comment.id)
            
            comment.reply('haHAA xD im 12 btw ;) \n\n\n\n\n\nI am a bot...beep boop | [Source code](https://github.com/joshbarbee/Reddit-bot)|[Complaints and Suggestions](https://docs.google.com/forms/d/e/1FAIpQLSc-wGMK5DKS5xuAAKfcLivc-nR92ycZXsbYp2Y0pBkfrCtrxA/viewform?usp=sf_link)')
            print("replied to comment[hahaa]: "+comment.id)
            repliedComments.append(comment.id)

            with open("repliedComments.txt", "a") as f:
                f.write(comment.id + "\n")
        
            print (repliedComments)
            time.sleep(30)
            print("Sleeping...")
        elif  "lol"in (comment.body) and comment.id not in repliedComments and not str(comment.author) == r.user.me() and len(comment.body)<4:
            print ("lol string found: "+ comment.id)
            
            comment.reply('When I use acronyms such as LOL or LMAO I use them not to express humor, but my crippling depression. They are a silent cry for help from this dark void of sadness. I used to use them genuinely, but as time went on I found myself meaning it less every time I used them. How many people actually laugh out loud when they say "LOL," laugh their ass off when they say "LMAO," and roll on the floor laughing when they say "ROFL"? No one. This is the result of the pathetic world of lies we live in. As my depression grew stronger over the years I found myself questioning the true meaning of these acronyms when I used them. I decided they represent the mask of anonymous lies we live behind on the internet and since they are lies it makes sense that the user is experiencing the opposite emotion of what they actually express. I used these "humorous" acronyms on a layer of irony for several more years but no one noticed. No one paid attention to my wounded calls for help, my desperate cries for relief from this horrible life. I now seek to solve this problem on my own instead of relying on the cruel, heartless "humans" that dominate society today. Tonight I solve the problem once and for all, by ending my trial on the hell we call "earth." LMAO 🔪 \n\n\n\n\n\nI am a bot...beep boop | [Source code](https://github.com/joshbarbee/Reddit-bot)|[Complaints and Suggestions](https://docs.google.com/forms/d/e/1FAIpQLSc-wGMK5DKS5xuAAKfcLivc-nR92ycZXsbYp2Y0pBkfrCtrxA/viewform?usp=sf_link)')
            #credits to previous pasta goes to u/tachankathegod
            print("replied to comment[lol]: "+comment.id)
            repliedComments.append(comment.id)

            with open("repliedComments.txt", "a") as f:
                f.write(comment.id + "\n")
        
            print (repliedComments)
            time.sleep(30)
            print("Sleeping...")
        elif "xD" in (comment.body) and comment.id not in repliedComments and not str(comment.author) == r.user.me() and len(comment.body)<3:
            print ("xD: "+ comment.id)
            
            comment.reply('ello judge jury i am here to discuss a burning issue in our subreddit the banning of the word "xd" as we all know we have used the word constantly throughout the life time of the subreddit but that still does not mean it can get annoying and or repetitive we have used xd so much that the word lost its meaning it is for the betterment of the subredditf we banned the usege of the word "xd"\n\n\n\n\n\nI am a bot...beep boop | [Source code](https://github.com/joshbarbee/Reddit-bot)|[Complaints and Suggestions](https://docs.google.com/forms/d/e/1FAIpQLSc-wGMK5DKS5xuAAKfcLivc-nR92ycZXsbYp2Y0pBkfrCtrxA/viewform?usp=sf_link)')
            #credits to previous pasta goes to u/blastgamez
            print("replied to comment[xD]: "+comment.id)
            repliedComments.append(comment.id)

            with open("repliedComments.txt", "a") as f:
                f.write(comment.id + "\n")
        
            print (repliedComments)
            time.sleep(30)
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
