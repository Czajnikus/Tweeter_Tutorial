import re


class Twitter(object):
    version = '1.0'

    def __init__(self):
        self.tweets = []

    def tweet(self, message):
        if len(message) >= 161:
            raise Exception('To long')
        self.tweets.append(message)

    def find_hashtag(self, message):
        return [m.lower() for m in re.findall('#(\w+)', message)]
