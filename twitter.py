import re

import os


class Twitter(object):
    version = '1.0'

    def __init__(self, backend=None):
        self.backend = backend
        self._tweets = []
        if self.backend and not os.path.exists(self.backend):
            with open(self.backend, "w"):
                pass

    def delete(self):
        print("It's the end")

    @property
    def tweets(self):
        return self._tweets

    def tweet(self, message):
        if len(message) >= 161:
            raise Exception('To long')
        self.tweets.append(message)

    def find_hashtags(self, message):
        return [m.lower() for m in re.findall("#(\w+)", message)]
