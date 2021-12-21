# pylint: disable=missing-docstring

from app.models import Tweet


class TweetRepository:
    def __init__(self):
        self.clear()

    def add(self, tweet):
        self.tweets.append(tweet)
        tweet.id = self.next_id
        self.next_id += 1
        return tweet

    def get(self, id):
        for tweet in self.tweets:
            if tweet.id == id:
                return tweet
        return None

    def clear(self):
        self.tweets = []
        self.next_id = 1
