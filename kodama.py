import praw
import time

REPLY_MESSAGE = "https://imgur.com/gallery/NgpcduR"


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('kodama-bot', user_agent="kodama bot 1.1!")
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit


def main():
    reddit = authenticate()
    while True:
        run_bot(reddit)


def run_bot(reddit):
    print("Obtaining 25 comments...")
    for comment in reddit.subreddit('test').comments(limit=25):
        if "kodama" in comment.body:
            print("comment with \"kodama\" found")
            comment.reply(REPLY_MESSAGE)
            print("Replied to comment: " + comment.id)

    print("Sleeping for one minute!")
    # Timeout for this bad boy, no spam allowed!
    time.sleep(60)


if __name__ == '__main__':
    main()
