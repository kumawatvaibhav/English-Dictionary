def api():
    from flask import Flask,jsonify
    import json 

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    @app.route('/readfile')
    def readfile():
        data = json.load(open('dictionary_compact.json'))
        return data

    if __name__ == "__main__":
        app.run(debug=True)

api()