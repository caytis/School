from flask import Flask, request, send_file, redirect, jsonify, render_template
from Steganography import hide_message, show_message
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode_image():
    if 'image' not in request.files:
        return redirect(request.url)
    image = request.files['image']
    message = request.form['message']
    
    try:
        encoded_image = hide_message(image, message)
        img_io = BytesIO()
        encoded_image.save(img_io, format='PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='hidden.png')
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route('/decode', methods=['POST'])
def decode_image():
    if 'image' not in request.files:
        return redirect(request.url)
    image = request.files['image']
    
    try:
        decoded_message = show_message(image)
        return render_template('index.html', decoded_message=decoded_message)
    except Exception as e:
        return str(e), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
