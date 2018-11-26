import pytest
from twitter import Twitter


@pytest.fixture(params=[None, "test.txt"])
def twitter(request):
    twitter = Twitter(backend=request.param)
    yield twitter
    twitter.delete()


def test_initization(twitter):
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
    assert twitter.find_hashtags(message) == expected
