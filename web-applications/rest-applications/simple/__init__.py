from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import datetime

app = Flask(__name__)
api = Api(app)


class Echo(Resource):
    def get(self):
        return {'application': 'simple rest application', 'timestamp': str(datetime.date.today())}

    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('comment', type=str, help='Comment to echo')
            args = parser.parse_args()

            _echoComment = args['comment']

            return {'application': 'simple rest application', 'comment': _echoComment}

        except Exception as e:
            return {'error': str(e)}

api.add_resource(Echo, '/echo')

if __name__ == '__main__':
    app.run(debug=True)