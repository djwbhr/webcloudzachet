from flask import Flask
from flask_restx import Api, Resource
import json

app = Flask(__name__)
api = Api(app, title='Evseev Zachet')

@api.route('/add/<number1>/<number2>')
class Addition(Resource):
    def get(self, number1, number2):
        try:
            num1 = float(number1)
            num2 = float(number2)
            result = num1 + num2
            return json.dumps({'status': True, 'answer': f'{result:.4f}'})
        except ValueError:
            return json.dumps({'status': False, 'answer': 'ARGS_PARSING_ERROR: Invalid numbers provided'}), 400

@api.route('/sub/<number1>/<number2>')
class Subtraction(Resource):
    def get(self, number1, number2):
        try:
            num1 = float(number1)
            num2 = float(number2)
            result = num1 - num2
            return json.dumps({'status': True, 'answer': f'{result:.4f}'})
        except ValueError:
            return json.dumps({'status': False, 'answer': 'ARGS_PARSING_ERROR: Invalid numbers provided'}), 400

@api.route('/mul/<number1>/<number2>')
class Multiplication(Resource):
    def get(self, number1, number2):
        try:
            num1 = float(number1)
            num2 = float(number2)
            result = num1 * num2
            return json.dumps({'status': True, 'answer': f'{result:.4f}'})
        except ValueError:
            return json.dumps({'status': False, 'answer': 'ARGS_PARSING_ERROR: Invalid numbers provided'})

@api.route('/div/<number1>/<number2>')
class Division(Resource):
    def get(self, number1, number2):
        try:
            num1 = float(number1)
            num2 = float(number2)
            if num2 == 0:
                return json.dumps({'status': False, 'answer': 'DIVISION_BY_ZERO'})
            result = num1 / num2
            return json.dumps({'status': True, 'answer': f'{result:.4f}'})
        except ValueError:
            return json.dumps({'status': False, 'answer': 'ARGS_PARSING_ERROR: Invalid numbers provided'})

if __name__ == '__main__':
    app.run(debug=True)
