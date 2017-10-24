import praw
import config
import time
import os
import threading

def bot_login():
    print('Logging in..')
    r = praw.Reddit(username=config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "haHAA bot haHAA responder v 0.2")
    print("Logged in...")
    return r
def run_bot(r,repliedComments, repliedReplies):
    
    for comment in r.subreddit('all').stream.comments():
        
        try:
            print(comment) 
           
            if "haHAA"in (comment.body) and comment.id not in repliedComments and not str(comment.author) == r.user.me():
                print ("HaHAA string found: "+ comment.id)
                
                comment.reply('haHAA xD im 12 btw ;) \n\n\n\n\n\nI am a bot...beep boop | [Source code](https://github.com/joshbarbee/Reddit-bot)|[Complaints and Suggestions](https://docs.google.com/forms/d/e/1FAIpQLSc-wGMK5DKS5xuAAKfcLivc-nR92ycZXsbYp2Y0pBkfrCtrxA/viewform?usp=sf_link)|!info for more')
                print("replied to comment[hahaa]: "+comment.id)
                repliedComments.append(comment.id)

                with open("repliedComments.txt", "a") as f:
                    f.write(comment.id + "\n")
            
                print (repliedComments)
                time.sleep(30)
                print("Sleeping...")
                replies()
                break
            elif  "lol"in (comment.body) and comment.id not in repliedComments and not str(comment.author) == r.user.me() and len(comment.body)<4:
                print ("lol string found: "+ comment.id)
                
                comment.reply('When I use acronyms such as LOL or LMAO I use them not to express humor, but my crippling depression. They are a silent cry for help from this dark void of sadness. I used to use them genuinely, but as time went on I found myself meaning it less every time I used them. How many people actually laugh out loud when they say "LOL," laugh their ass off when they say "LMAO," and roll on the floor laughing when they say "ROFL"? No one. This is the result of the pathetic world of lies we live in. As my depression grew stronger over the years I found myself questioning the true meaning of these acronyms when I used them. I decided they represent the mask of anonymous lies we live behind on the internet and since they are lies it makes sense that the user is experiencing the opposite emotion of what they actually express. I used these "humorous" acronyms on a layer of irony for several more years but no one noticed. No one paid attention to my wounded calls for help, my desperate cries for relief from this horrible life. I now seek to solve this problem on my own instead of relying on the cruel, heartless "humans" that dominate society today. Tonight I solve the problem once and for all, by ending my trial on the hell we call "earth." LMAO 🔪 \n\n\n\n\n\nI am a bot...beep boop | [Source code](https://github.com/joshbarbee/Reddit-bot)|[Complaints and Suggestions](https://docs.google.com/forms/d/e/1FAIpQLSc-wGMK5DKS5xuAAKfcLivc-nR92ycZXsbYp2Y0pBkfrCtrxA/viewform?usp=sf_link)!info for more')
                #credits to previous pasta goes to u/tachankathegod
                print("replied to comment[lol]: "+comment.id)
                repliedComments.append(comment.id)

                with open("repliedComments.txt", "a") as f:
                    f.write(comment.id + "\n")
            
                print (repliedComments)
                time.sleep(60)
                replies()
                print("Sleeping...")
                break
            else:
                break
            
        except Exception as e:
            pass   
    def replies():
        for reply in r.inbox.comment_replies():
            try:
                if reply.author != r.user.me() and "!info" in (reply.reply(body)) and reply.id not in repliedReplies:
                    reply.reply('This bot was made with the intentions of triggering as many redditors as possible.')
                    #credits to previous pasta goes to u/tachankathegod
                    print("replied to comment[trigger]: "+reply.id)
                    repliedComments.append(comment.id)

                    with open("repliedReplies.txt", "a") as f:
                        f.write(reply.id + "\n")
                    
                    print (repliedReplies)
                    time.sleep(30)
                    print("Sleeping...")
                elif reply.author != r.user.me() and "bad bot" in (reply.body):
                    reply.reply('Bad human.')
                    #credits to previous pasta goes to u/tachankathegod
                    print("replied to comment[bad human]: "+reply.id)
                    repliedReplies.append(reply.id)

                    with open("repliedReplies.txt", "a") as f:
                        f.write(reply.id + "\n")
                    
                    print (repliedReplies)
                    time.sleep(30)
                    print("Sleeping...")
                    break
                elif reply.author != r.user.me() and "good bot" in (reply.body):
                    reply.reply('good human, god human.')
                    #credits to previous pasta goes to u/tachankathegod
                    print("replied to comment[bad human]: "+reply.id)
                    repliedReplies.append(reply.id)

                    with open("repliedReplies.txt", "a") as f:
                        f.write(reply.id + "\n")
                    
                    print (repliedReplies)
                    time.sleep(30)
                    print("Sleeping...")
                    break
            
            except Exception as e:
                pass   
def savedComments():
    if not os.path.isfile("repliedComments.txt"):
        repliedComments = []
    else:
        with open("repliedComments.txt", "r") as f:
            repliedComments = f.read()
            repliedComments = repliedComments.split("\r")
            repliedComments = list(filter(None, repliedComments))

    return repliedComments
def savedReplies():
    if not os.path.isfile("repliedReplies.txt"):
        repliedreplies = []
    else:
        with open("repliedReplies.txt", "r") as f:
            repliedReplies = f.read()
            repliedReplies = repliedReplies.split("\r")
            repliedReplies = list(filter(None, repliedReplies))

    return repliedComments


r = bot_login()
repliedComments = savedComments()
repliedReplies=savedReplies

while True:
    run_bot(r, repliedComments,repliedReplies)
print (repliedComment,repliedReplies)
