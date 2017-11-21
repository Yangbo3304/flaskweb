# -*- coding: utf-8 -*-
from application import app


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return "kk"


