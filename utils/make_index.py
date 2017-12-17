from twitter_search import get_tweets

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
        print(wordlist)
        for word in wordlist:
            d.setdefault(word,[])
            d[word].append(tweet)
    return d

def make_index(coin):
    tweets = get_tweets(coin)
    ind = index_maker(tweets)
    file = open('tweets.txt','w' )
    file.write(str(ind))
    #print(tweets)
    #file.write(str(tweets))
    file.close()
    return ind
    #return tweets

'''
tweets = [
'BTC is really good',
'I dont really like btc',
'BTC gets me so hard'
]

print(index_maker(tweets))
'''
#print(index_maker(["I love btc hey chicken","I love btc hey chicken lol"]))
