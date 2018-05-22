#-*- coding:utf-8 -*-

from flask import Flask
import lotto_analysis as lotto

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'test'

@app.route('/lottoNumbers')
def get_lotto():
    return str(lotto.getRecommendNumbers())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
