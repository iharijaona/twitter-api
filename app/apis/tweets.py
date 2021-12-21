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
    @api.marshal_with(TweetModel)
    def get(self, id):
        tweet = tweet_repository.get(id)
        if tweet is None:
            api.abort(404)
        else:
            return tweet
