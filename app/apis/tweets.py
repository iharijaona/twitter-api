# pylint: disable=missing-docstring

from app.models import Tweet
from flask_restx import Namespace, Resource, fields
from app.db import tweet_repository

api = Namespace('tweets')

TweetModel = api.model('Tweet', {
    'id': fields.Integer(required=True),
    'text': fields.String(required=True),
    'created_at': fields.DateTime(required=True),
})

TweetInput = api.model('TweetInput', {
    'text': fields.String(required=True),
})


@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
@api.param('id', 'The tweet unique identifier')
class TweetResource(Resource):
    @api.doc('get_tweet')
    @api.marshal_with(TweetModel)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet


@api.route('/')
class TweetListResource(Resource):
    @api.doc('list_tweets')
    @api.marshal_list_with(TweetModel)
    def get(self):
        '''List all tweets'''
        return tweet_repository.tweets

    @api.doc('create_tweet')
    @api.expect(TweetInput)
    @api.marshal_with(TweetModel, code=201)
    def post(self):
        '''Create a new tweet'''
        return tweet_repository.add(Tweet(api.payload['text'])), 201
