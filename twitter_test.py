import pytest
from twitter import Twitter

@pytest.fixture
def twitter():
    twitter = Twitter()
    return twitter

def test_initization(twitter):
    twitter = Twitter()
    assert twitter


def test_message(twitter):
    twitter.tweet('Tekst wiadomosci')
    assert twitter.tweets == ['Tekst wiadomosci']


def test_tweet_lenght(twitter):
    with pytest.raises(Exception):
        twitter.tweet('Tekst wiadomosci'*120)
    assert twitter.tweets == []

@pytest.mark.parametrize('message, expected', (
        ('Test #first message', ['first']),
        ('#first Test message', ['first']),
        ('Test message #first ', ['first']),
        ('Test message #FIRST ', ['first']),
        ('Test #FIRST message #SECOND', ['first', 'second'])
))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.find_hashtag(message) == expected

