
import twitter
import time
import subprocess

#get keys from https://apps.twitter.com/
CONSUMER_KEY = 'WWWWW'
CONSUMER_SECRET = 'XXXXXX'
ACCESS_TOKEN = 'ZZZZZZ'
ACCESS_TOKEN_SECRET = 'YYYYYYY'

SEARCH = '@ACOECore' #can also search #hashtags too

t = twitter.Twitter(auth=twitter.OAuth(ACCESS_TOKEN, ACCESS_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET))
oldTweet=''
checkTweet=''
while True:
    while oldTweet==checkTweet:
        time.sleep(10)
        checkTweet=t.search.tweets(q=SEARCH)['statuses'][0]['text']
    print(checkTweet)
    subprocess.call('espeak -v en-uk "' + checkTweet+'"', shell=True)
    oldTweet=checkTweet
