from flask import Flask, jsonify
from models import *
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/v1/sales', methods=['GET'])
def get_all():
    all_sales = Sales().get_all_sales()
    data = jsonify([_.serialize() for _ in all_sales])
    # print(data)

    return data


if __name__ == '__main__':
    app.run(debug=True)
