import twitter

api = twitter.Api(consumer_key='',
                      consumer_secret='',
                      access_token_key='',
                      access_token_secret='')
def get_tweets(coin_name):
    ret_list = []
    query = "q=" + coin_name + "&result_type=recent&count=100"
    results = api.GetSearch(raw_query = query)
    for sent in results:
        print(sent.text.encode('ascii', errors='ignore'))
        ret_list.append(sent.text)
    return ret_list
