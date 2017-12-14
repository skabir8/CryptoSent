import twitter

api = twitter.Api(consumer_key='vdbaYse0QnknbPGOCFRvG5Y60',
                      consumer_secret='ZVWpCARqpE8llzFOH4j875CiwZykJ7Nhg3ccDSOcE6ro6IXjhW',
                      access_token_key='911995423690231809-5jA2hmYgP8qAAHwDyyHifjvlDEDV3en',
                      access_token_secret='Sqazu1ta7PWois0MiW2krZ155D7M0N8MHchFTwQ0PFUyn')
def get_tweets(coin_name):
    results = api.GetSearch(raw_query="q=btc&result_type=recent")
    print(results)



get_tweets('btc')
