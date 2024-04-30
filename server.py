from flask import Flask, request, send_file, render_template, redirect, url_for
import os
from Steganography import hide_message, show_message
from PIL import Image
import io

app = Flask(__name__)

# Folder to store uploaded and processed images
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def index():
#     # Render the HTML file
#     return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode_message():
    if request.method == 'POST':
        # Check if the file part is present in the request
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']
        message = request.form['message']

        if file.filename == '':
            return redirect(request.url)
        
        if file and message:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)  # Save the original image

            # Open the image and encode the message
            img = Image.open(filename)
            encoded_img = hide_message(img, message)  # Assuming encode function modifies the image and returns it

            # Save the encoded image
            encoded_filename = f'encoded_{file.filename}'
            path_to_save = os.path.join(app.config['UPLOAD_FOLDER'], encoded_filename)
            encoded_img.save(path_to_save)

            # Send the encoded image back to the client
            return send_file(path_to_save, as_attachment=True)

    return 'Something went wrong', 400

@app.route('/decode', methods=['POST'])
def decode_message():
    if request.method == 'POST':
        if 'image' not in request.files:
            return redirect(request.url)
        file = request.files['image']

        if file.filename == '':
            return redirect(request.url)

        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)  # Save the uploaded image

            # Open the image and decode the message
            img = Image.open(filename)
            hidden_message = show_message(img)  # Assuming decode function retrieves the message

            return f'Decoded message: {hidden_message}'

    return 'Something went wrong', 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)
