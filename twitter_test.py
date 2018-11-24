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


def test_tweet_with_hashtag():
    twitter = Twitter()
    message = 'Test #first message '
    twitter.tweet(message)
    assert 'first' in twitter.find_hashtag(message)

def test_tweet_with_hashtag_on_beggining():
    twitter = Twitter()
    message = '#first Test message '
    twitter.tweet(message)
    assert 'first' in twitter.find_hashtag(message)

def test_tweet_with_hashtag_on_ending():
    twitter = Twitter()
    message = 'Test message #first '
    twitter.tweet(message)
    assert 'first' in twitter.find_hashtag(message)

def test_tweet_with_hashtag_upper():
    twitter = Twitter()
    message = 'Test message #FIRST '
    twitter.tweet(message)
    assert 'FIRST' in twitter.find_hashtag(message)



