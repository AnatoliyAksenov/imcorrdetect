#!flask/bin/python
from flask import Flask, jsonify
from flask import request, send_file
import io
import model
import base64
import tempfile
import os
from PIL import Image


app = Flask(__name__, static_folder='public/app', static_url_path='')

@app.route('/')
def index():
    return send_file("public/app/index.html")


@app.route('/api/predict', methods=['GET','POST'])
def post():
    # imgfile = tempfile.NamedTemporaryFile(delete=False)
    # imgfile.write(request.files['file']) 
    # imgfile.close()
    f = request.files['file']
    f.save('temp.bin')
    image_binary = model.predict('temp.bin')

    # image_binary = model.predict(imgfile.name)
    # image_binary = model.predict('buzova.jpg')

    fff = io.BytesIO()
    img = Image.fromarray(image_binary)

    img.save(fff, 'PNG')
    fff.seek(0)

    return send_file(fff, mimetype='image/png', as_attachment=True, attachment_filename='result.png')

if __name__ == '__main__':
    port = int(os.environ['PORT']) or 8080
    app.run(host='0.0.0.0', port=port, debug=False)