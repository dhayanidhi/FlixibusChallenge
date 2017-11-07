#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, abort, jsonify

from src.starter import get_sorted_result

app = Flask(__name__)

@app.route('/challenge/model', methods=['GET'])
def index():
    if not request.json:
        abort(400)

    body = request.json["features"]
    output_result = get_sorted_result(body)
    return jsonify({'rank':output_result}), 200

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()