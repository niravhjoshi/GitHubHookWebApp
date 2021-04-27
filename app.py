
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello from Nirav Joshi's flask application testing for GitHub WebHooks!"

@app.route('/apiGitHubWebHook/', methods=['POST'])
def GetDataFromGitHubWHooks():
    data = request.get_json()
    print(data)
    '''logic for manupulating this data will be discuss based on TBD'''
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
