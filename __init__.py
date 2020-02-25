from flask import Flask, request, Response, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_data():
    uploaded_files = request.files.getlist("file")
    for file in uploaded_files:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            print(file)
    return {}, 200

@app.route('/test', methods=['POST'])
def test():
    return {"message": "Server connection test complete! Go to calibrate work."}, 200

app.run(port=5000, host='0.0.0.0', debug=True, threaded=True) # 192.168.0.37