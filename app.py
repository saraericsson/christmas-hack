from flask import Flask, escape, url_for
from alpha_vantage.techindicators import TechIndicators

import config

app = Flask(__name__)

@app.route('/')
def index():
    return 'Christmas Hack, YOLO'

@app.route('/sma/<symbol>')
def sma(symbol):
    ti = TechIndicators(key=config.alpha_vantage_key)
    data = ti.get_sma(symbol=symbol, time_period=50)

    return 'SMA50 2019-12-24: {}'.format(escape(data[0]['2019-12-24']['SMA']))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('sma', symbol='AAPL'))
