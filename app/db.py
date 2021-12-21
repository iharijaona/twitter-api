from .models import Tweet
from .repositories import TweetRepository

tweet_repository = TweetRepository()
tweet_repository.add(Tweet("a first tweet"))
tweet_repository.add(Tweet("a second tweet"))
