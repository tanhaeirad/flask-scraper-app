from flask import Flask, request
from flask_restful import Resource, Api
from scraper import lambda_handler

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def post(self):
        data = request.get_json()  # Parse JSON input from the request
        return lambda_handler(data, None)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
