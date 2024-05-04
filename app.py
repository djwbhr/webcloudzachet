from flask import Flask, jsonify
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Evseev Zachet')

@api.route('/add/<number1>/<number2>')
class Addition(Resource):
    def get(self, number1, number2):
        try:
            num1 = float(number1)
            num2 = float(number2)
            result = num1 + num2
            return jsonify({'status': True, 'answer': f'{result:.4f}'})
        except ValueError:
            return jsonify({'status': False, 'answer': 'ARGS_PARSING_ERROR: Invalid numbers provided'}), 400
        except Exception as e:
            return jsonify({'status': False, 'answer': f'ERROR: {str(e)}'}), 400

@api.route('/sub/<number1>/<number2>')
class Subtraction(Resource):
    def get(self, number1, number2):
        try:
            num1 = float(number1)
            num2 = float(number2)
            result = num1 - num2
            return jsonify({'status': True, 'answer': f'{result:.4f}'})
        except ValueError:
            return jsonify({'status': False, 'answer': 'ARGS_PARSING_ERROR: Invalid numbers provided'}), 400
        except Exception as e:
            return jsonify({'status': False, 'answer': f'ERROR: {str(e)}'}), 400

@api.route('/mul/<number1>/<number2>')
class Multiplication(Resource):
    def get(self, number1, number2):
        try:
            num1 = float(number1)
            num2 = float(number2)
            result = num1 * num2
            return jsonify({'status': True, 'answer': f'{result:.4f}'})
        except ValueError:
            return jsonify({'status': False, 'answer': 'ARGS_PARSING_ERROR: Invalid numbers provided'}), 400
        except Exception as e:
            return jsonify({'status': False, 'answer': f'ERROR: {str(e)}'}), 400

@api.route('/div/<number1>/<number2>')
class Division(Resource):
    def get(self, number1, number2):
        try:
            num1 = float(number1)
            num2 = float(number2)
            if num2 == 0:
                raise ZeroDivisionError('DIVISION_BY_ZERO')
            result = num1 / num2
            return jsonify({'status': True, 'answer': f'{result:.4f}'})
        except ValueError:
            return jsonify({'status': False, 'answer': 'ARGS_PARSING_ERROR: Invalid numbers provided'}), 400
        except ZeroDivisionError:
            return jsonify({'status': False, 'answer': 'DIVISION_BY_ZERO'}), 400
        except Exception as e:
            return jsonify({'status': False, 'answer': f'ERROR: {str(e)}'}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
