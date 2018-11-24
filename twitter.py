class Twitter(object):
    version = '1.0'

    def __init__(self):
        self.tweets = []

    def tweet(self, message):
        if len(message) >= 161:
            raise Exception('To long')
        elif len(message) < 161:
            self.tweets.append(message)

