from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Yüklenen dosyaların kaydedileceği dizin
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Yalnızca izin verilen dosya uzantıları
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', 'mov'}

WISHES_FILE = os.path.join(UPLOAD_FOLDER, 'wishes.json')


# Dosya uzantısının izin verilip verilmediğini kontrol et
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_wishes():
    if os.path.exists(WISHES_FILE):
        with open(WISHES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_wishes(wishes):
    with open(WISHES_FILE, 'w') as f:
        json.dump(wishes, f, indent=4)

wishes = load_wishes()

@app.route('/submit_wish', methods=['POST'])
def submit_wish():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')

    if not name or not message:
        return jsonify({'error': 'Name and message are required!'}), 400

    wish = {'name': name, 'message': message}
    wishes.append(wish)
    save_wishes(wishes)
    return jsonify({'message': 'Dilek başarıyla eklendi!', 'wish': wish}), 200

@app.route('/get_wishes', methods=['GET'])
def get_wishes():
    return jsonify(wishes), 200

# Dosya yükleme endpoint'i
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return jsonify({
            'message': 'Dosya başarıyla yüklendi!',
            'filename': filename,
            'filepath': filepath
        })
    else:
        return jsonify({'error': 'File type not allowed'}), 400

# Yüklenen dosyaları statik olarak sunmak için endpoint
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Not bırakma endpoint'i
@app.route('/submit_note', methods=['POST'])
def submit_note():
    name = request.form.get('name')
    note = request.form.get('note')
    video = request.files.get('video')

    if not name or not note or not video:
        return jsonify({'error': 'Name, note, and video are required!'}), 400

    if video and allowed_file(video.filename):
        filename = secure_filename(video.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        video.save(filepath)

        # JSON formatında notu kaydet
        note_data = {
            'name': name,
            'note': note,
            'video': filename
        }

        notes_file = os.path.join(UPLOAD_FOLDER, 'notes.json')

        # Mevcut notları yükle
        if os.path.exists(notes_file):
            with open(notes_file, 'r') as f:
                notes = json.load(f)
        else:
            notes = []

        # Yeni notu ekle
        notes.append(note_data)

        # Notları kaydet
        with open(notes_file, 'w') as f:
            json.dump(notes, f, indent=4)

        return jsonify({
            'message': 'Not başarıyla kaydedildi!',
            'note': note_data
        })
    else:
        return jsonify({'error': 'Video type not allowed'}), 400

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=3000)
