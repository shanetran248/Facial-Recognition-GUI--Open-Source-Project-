from flask import Flask, render_template, request, redirect, url_for
import os
import face_recognition
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static')

# Configure upload folders
KNOWN_FOLDER = 'known_persons'
UNKNOWN_FOLDER = 'unknown_persons'

# Ensure folders exist
os.makedirs(KNOWN_FOLDER, exist_ok=True)
os.makedirs(UNKNOWN_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_known', methods=['POST'])
def upload_known():
    file = request.files['known_image']
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(KNOWN_FOLDER, filename))
    return redirect(url_for('index'))

@app.route('/upload_unknown', methods=['POST'])
def upload_unknown():
    file = request.files['unknown_image']
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UNKNOWN_FOLDER, filename)
        file.save(file_path)
        # Perform facial recognition
        result = recognize_face(file_path)
        # Check recognition result and prepare message and status for result page
        if result:
            message = "Face recognized in known persons!"
            status = "success"
        else:
            message = "Face not recognized."
            status = "error"
        # Render the result page with the message and status
        return render_template('result.html', message=message, status=status)
    return redirect(url_for('index'))

def recognize_face(unknown_image_path):
    # Load the uploaded unknown image
    unknown_image = face_recognition.load_image_file(unknown_image_path)
    unknown_encoding = face_recognition.face_encodings(unknown_image)
    
    if not unknown_encoding:
        return False  # No faces found in the unknown image
    unknown_encoding = unknown_encoding[0]
    
    # Compare with known faces
    for filename in os.listdir(KNOWN_FOLDER):
        known_image_path = os.path.join(KNOWN_FOLDER, filename)
        known_image = face_recognition.load_image_file(known_image_path)
        known_encodings = face_recognition.face_encodings(known_image)
        
        for known_encoding in known_encodings:
            results = face_recognition.compare_faces([known_encoding], unknown_encoding)
            if results[0]:
                return True  # Face recognized
    
    return False  # Face not recognized

if __name__ == '__main__':
    app.run(debug=True)

