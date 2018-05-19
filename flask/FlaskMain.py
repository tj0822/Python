#-*- coding:utf-8 -*-

from flask import Flask
import lotto.lotto_analysis as lotto
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'test'

@app.route('/lottoNumbers')
def get_lotto():
    return lotto.getRecommendNumbers()

if __name__ == '__main__':
    app.run(port=5000, debug=True)