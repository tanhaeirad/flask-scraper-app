from flask import Flask
from flask_restful import Resource, Api
from scraper import lambda_handler

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return lambda_handler({'queryStringParameters': {'county_name': 'Richland', 'date': '07/28/2023'}}, None)

        # return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
