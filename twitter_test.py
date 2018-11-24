from twitter import Twitter

def test_initization():
    twitter = Twitter()
    assert twitter

def test_message():
    twitter = Twitter()
    twitter.tweet('dupa')
    assert twitter.tweets == ['dupa']

def test_tweet_lenght():
    twitter = Twitter()
    twitter.tweet('dupa'*120)
    assert twitter.tweets == ['dupa'*120]