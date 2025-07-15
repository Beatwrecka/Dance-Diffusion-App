from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    print("Generating audio with:", data)
    return jsonify({"status": "success", "message": "Audio generation initiated", "input": data})

if __name__ == '__main__':
    app.run(debug=True)
