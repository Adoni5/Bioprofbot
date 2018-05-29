from twython import Twython, TwythonError
import time
import os

ckey = os.environ.get("ckey")
skey = os.environ.get("skey")
access_token = os.environ.get("access_token")
access_token_secret = os.environ.get("access_token_secret")

twitter = Twython(ckey, skey,
                  access_token, access_token_secret)
try:
    with open('liners.txt', 'r+') as tweetfile:
        buff = tweetfile.readlines()

    for line in buff[:]:
        line = line.strip(r'\n')
        if len(line) <= 140 and len(line) > 0:
            print("Tweeting...")
            twitter.update_status(status=line)
            with open('liners.txt', 'w') as tweetfile:
                buff.remove(line)
                tweetfile.writelines(buff)
            time.sleep(900)
        else:
            with open('liners.txt', 'w') as tweetfile:
                buff.remove(line)
                tweetfile.writelines(buff)
            print("Skipped line - Char length violation")
            continue
    print("No more lines to tweet...")


except TwythonError as e:
    print(e)
