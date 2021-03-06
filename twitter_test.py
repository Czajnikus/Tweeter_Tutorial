import pytest
from twitter import Twitter



@pytest.fixture
def backend(tmpdir):
    temp_file = tmpdir.join('test.txt')
    temp_file.write('')
    return temp_file

@pytest.fixture(params=['list', 'backend'], name="twitter")
def fixture_twitter(backend, request):
    if request.param == 'list':
        twitter = Twitter()
    elif request.param == 'backend':
        twitter = Twitter(backend=backend)
    return twitter


def test_initization(twitter):
    assert twitter


def test_message(twitter):
    twitter.tweet('Tekst wiadomosci')
    assert twitter.tweets == ['Tekst wiadomosci']


def test_tweet_lenght(twitter):
    with pytest.raises(Exception):
        twitter.tweet('Tekst wiadomosci'*120)
    assert twitter.tweets == []

def test_initialize_two_twitter_classes(backend):
    twitter1 = Twitter(backend=backend)
    twitter2 = Twitter(backend=backend)

    twitter1.tweet('Test 1')
    twitter1.tweet('Test 2')

    assert twitter2.tweets == ['Test 1', 'Test 2']

@pytest.mark.parametrize('message, expected', (
        ('Test #first message', ['first']),
        ('#first Test message', ['first']),
        ('Test message #first ', ['first']),
        ('Test message #FIRST ', ['first']),
        ('Test #FIRST message #SECOND', ['first', 'second'])
))
def test_tweet_with_hashtag(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected
