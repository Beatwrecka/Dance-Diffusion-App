from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='public', static_url_path='/public')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/generate', methods=['POST'])
def generate():
    return jsonify({'status': 'ok', 'audio': 'demo.wav'})

@app.route('/train', methods=['POST'])
def train():
    return jsonify({'status': 'started'})

@app.route('/upload', methods=['POST'])
def upload():
    os.makedirs('uploads', exist_ok=True)
    uploaded_files = request.files.getlist('files')
    saved = []
    for f in uploaded_files:
        path = os.path.join('uploads', f.filename)
        f.save(path)
        saved.append(f.filename)
    return jsonify({'saved': saved, 'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
