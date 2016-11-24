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
        "consumer_key": "mAkZrHbOALk8SwZPDjX2u2oId",
        "consumer_secret": "LCcPyPk8OJZMQanT92wRDCjKXH1U7Z7aoY0uk9F6Rgrqh3bpkT",
        "access_token": "338528614-IIdsKVL7OvJP6EXelfxdLGzBYdxT6s19SgfqUpJ0",
        "access_token_secret": "OlDQLB0PlLhYNjFPuZmcflT5b47kYoCo22jLa9xB1tqwV"
    }

    api = get_api(cfg)
    tweet = tweet_input
    status = api.update_status(status=tweet)
    print '\n Tweet send: \n'
    # Yes, tweet is called 'status' rather confusing


while tweeting:
    main()
