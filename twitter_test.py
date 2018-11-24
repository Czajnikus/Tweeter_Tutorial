from twitter import Twitter

def test_initization():
    twitter = Twitter()
    assert twitter

def test_message():
    twitter = Twitter()
    twitter.tweet('Tekst wiadomosci')
    assert twitter.tweets == ['Tekst wiadomosci']

def test_tweet_lenght():
    twitter = Twitter()
    twitter.tweet('Tekst wiadomosci'*120)
    assert twitter.tweets == ['Tekst wiadomosci'*120]