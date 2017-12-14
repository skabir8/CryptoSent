def make_index(tweets):
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

tweets = [
'BTC is really good',
'I dont really like btc',
'BTC gets me so fucking hard'
]

print(make_index(tweets))
