import praw
import config
import time
import os

def bot_login():
    print("Logging in...")
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "kodama bot 1.0!")
    print("Logged in!")

    return r


def run_bot(r, comments_replied_to):
    print("Obtaining 20 comments...")

    for comment in r.subreddit('test').comments(limit=20):
        if "kodama" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
            print("comment with \"kodama\" found")
            comment.reply("https://imgur.com/gallery/NgpcduR")
            print("Replied to comment: " + comment.id)

            comments_replied_to.append(comment.id)

            with open ("comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")
    

    print("Sleeping for one minute!")
    #Timeout for this bad boy, no spam allowed!
    time.sleep(60)


def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))
    
    return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print(comments_replied_to)

while True:
    run_bot(r, comments_replied_to)