from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__) # এখানে ভেরিয়েবলের নাম 'app' হতে হবে
CORS(app)

@app.route('/')
def home():
    return "পাইথন ওয়েব সার্ভার সচল আছে!"

@app.route('/healthz')
def health_check():
    return "OK", 200

@app.route('/api/hello')
def hello():
    return jsonify({
        "message": "হ্যালো! আপনি সফলভাবে পাইথন সার্ভারের সাথে যুক্ত হয়েছেন।",
        "status": "success"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
