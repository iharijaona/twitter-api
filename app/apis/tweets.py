# pylint: disable=missing-docstring

from flask_restx import Namespace, Resource, fields
from app.db import tweet_repository

api = Namespace('tweets')

TweetModel = api.model('Tweet', {
    'id': fields.Integer,
    'text': fields.String,
    'created_at': fields.DateTime
})


@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
@api.param('id', 'The tweet unique identifier')
class TweetResource(Resource):
    @api.doc('get_cat')
    @api.marshal_with(TweetModel)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet


@api.route('/')
class TweetListResource(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(TweetModel)
    def get(self):
        return tweet_repository.tweets
