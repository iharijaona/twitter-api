from flask_testing import TestCase
from app import create_app
from app.models import Tweet
from app.db import tweet_repository


class TestTweetViews(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def setUp(self):
        tweet_repository.clear()

    def test_tweet_show(self):
        first_tweet = Tweet("First tweet")
        tweet_repository.add(first_tweet)
        response = self.client.get("/tweets/1")
        response_tweet = response.json
        self.assertEqual(response_tweet["id"], 1)
        self.assertEqual(response_tweet["text"], "First tweet")
        self.assertIsNotNone(response_tweet["created_at"])

    def test_tweets_show(self):
        first_tweet = Tweet("First tweet")
        tweet_repository.add(first_tweet)
        response = self.client.get("/tweets/")
        response_tweets = response.json
        self.assertIsInstance(response_tweets, list)
        self.assertEqual(response_tweets[0]["id"], 1)
        self.assertEqual(response_tweets[0]["text"], "First tweet")
        self.assertIsNotNone(response_tweets[0]["created_at"])

    def test_tweet_create(self):
        response = self.client.post("/tweets/", json={
            "text": "The created tweet"
        })
        response_tweet = response.json
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response_tweet["id"], int)
        self.assertEqual(response_tweet["text"], "The created tweet")
        self.assertIsNotNone(response_tweet["created_at"])
