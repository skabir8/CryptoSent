from utils.twitter_search import get_tweets

def index_maker(tweets):
    d={}
    for tweet in tweets:
        cleantext = ""
        for letter in tweet:
            if letter.isalpha():
                cleantext = cleantext + letter.lower()
            else:
                cleantext = cleantext + " "
        wordlist = cleantext.split()
        for word in wordlist:
            d.setdefault(word,[])
            d[word].append(tweet)
    return d

def make_index(coin):
    tweets = get_tweets(coin)
    #for tweet in tweets:
#        print tweet
#        print ""
#        print "jordan"
#        print ""
    ind = index_maker(tweets)
    return ind
    #return tweets

'''
tweets = [
'BTC is really good',
'I dont really like btc',
'BTC gets me so hard'
]
'''

#print(make_index('btc')['up'])

#print(index_maker(["I love btc hey chicken","I love btc hey chicken lol"]))
#print(make_index('btc')['time'])
