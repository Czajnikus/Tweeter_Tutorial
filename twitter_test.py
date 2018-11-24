import pytest
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
    with pytest.raises(Exception):
        twitter.tweet('Tekst wiadomosci'*120)
    assert twitter.tweets == []

@pytest.mark.parametrize('message, hashtag', (
        ('Test #first message', 'first'),
        ('#first Test message', 'first'),
        ('Test message #first ', 'first'),
        ('Test message #FIRST ', 'FIRST')
))
def test_tweet_with_hashtag(message, hashtag):
    twitter = Twitter()
    assert hashtag in twitter.find_hashtag(message)

