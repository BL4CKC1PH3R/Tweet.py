import sys
import tweepy

tweeting = True
times_tweet = 0

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


def main():
    if times_tweet == 0:
        tweet_input = raw_input('Write your Tweet \n')
    else:
        tweet_input = raw_input('Write another Tweet \n')
    if tweet_input == 'exit':
        sys.exit(0)

# Fill in the values noted in previous step here
    cfg = {
    "consumer_key"        : "VALUE",
    "consumer_secret"     : "VALUE",
    "access_token"        : "VALUE",
    "access_token_secret" : "VALUE" 
    }

    api = get_api(cfg)
    tweet = tweet_input
    status = api.update_status(status=tweet)
    print '\n Tweet send: \n'
    # Yes, tweet is called 'status' rather confusing


while tweeting:
    main()
