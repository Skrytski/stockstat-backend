# import json
from decimal import Decimal
from flask import Flask, jsonify
from models import *
from flask.json import dumps
import datetime
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
    elif isinstance(o, Decimal):
        return str(o)


@app.route('/api/v1/year-sales', methods=['GET'])
def get_all():
    query = (Sales
             .select(Sales.date, fn.COUNT(Sales.image), fn.SUM(Sales.sum))
             .group_by(Sales.date))
    data = dumps([row for row in query.dicts()], indent=1,
                 default=default, sort_keys=False)
    return data


if __name__ == '__main__':
    app.run(debug=True)
