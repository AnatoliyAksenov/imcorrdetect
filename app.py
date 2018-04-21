#!flask/bin/python
from flask import Flask, jsonify
from flask import request, send_file
import io
import model
import base64
import tempfile
import os

app = Flask(__name__, static_folder='public/app', static_url_path='')

@app.route('/')
def index():
    return send_file("public/app/index.html")


@app.route('/api/document/gettype', methods=['POST'])
def post():
    imgfile = tempfile.NamedTemporaryFile(delete=False)
    imgfile.write(base64.b64decode(request.json['file'])) 
    imgfile.close()
    classes = model.predict(imgfile.name)
    result = {}
    result['classes'] = classes.tolist()
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ['PORT']) or 8080
    app.run(host='0.0.0.0', port=port, debug=False)