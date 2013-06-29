import twitter
from re import sub

con_secret='0tP6exUuP2nxHbYUmNcQDg'
con_secret_key='qx4QDMBNjs82gORi41SRxS8Vqg1ceTY3roxAy5KIo'
token='496688546-W1uw9iSt8BwWevWWP5pBYs5csPGAhhtjYQPGjSiY'
token_key='XzqvaobgvUfCiGEZ5Gxo6sZkab2YDdTC8PegyzVY'

def make_tweet(text):
    words = text[-140:]
    tweet = sub("[\"()-]", '', words)

    for t in range(len(tweet)):
        if tweet[t] == ' ':
            no_space = tweet[t+1:]
            break
        else:
            continue

    char = no_space[0]
    cap_it = char.capitalize()
    tweet_status = cap_it + no_space[1:]

    my_auth = twitter.OAuth(token, token_key, con_secret, con_secret_key)
    twit = twitter.Twitter(auth=my_auth)
    twit.statuses.update(status=tweet_status)

    print "\vYour status has been updated:\n", tweet_status

    return tweet_status
