import os
import json
import pysrt
from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
from deep_translator import GoogleTranslator
from threading import Thread

app = Flask(__name__, template_folder="templates")
UPLOAD_FOLDER = 'uploads'
PROGRESS_FILE = 'progress.json'
ALLOWED_EXTENSIONS = {'srt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024  # 2MB limit
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
progress_data = {"progress": 0.0, "filename": ""}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def translate_srt(input_path, output_path, source_lang, target_lang):
    subs = pysrt.open(input_path)
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    total = len(subs)

    for idx, sub in enumerate(subs):
        try:
            sub.text = translator.translate(sub.text)
        except Exception as e:
            print(f"Translation error at line {sub.index}: {e}")
        progress = round(((idx + 1) / total) * 100, 2)
        progress_data["progress"] = progress
        with open(PROGRESS_FILE, 'w') as f:
            json.dump(progress_data, f)

    subs.save(output_path, encoding='utf-8')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    source_lang = request.form.get('source_lang', 'en')
    target_lang = request.form.get('target_lang', 'ar')

    if not file or not allowed_file(file.filename):
        return jsonify({"success": False, "error": "Only .srt files are allowed."})

    filename = secure_filename(file.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_filename = f"translated_{filename}"
    output_path = os.path.join(UPLOAD_FOLDER, output_filename)

    file.save(input_path)
    progress_data["progress"] = 0.0
    progress_data["filename"] = output_filename
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress_data, f)

    thread = Thread(target=translate_srt, args=(input_path, output_path, source_lang, target_lang))
    thread.start()

    return jsonify({"success": True, "filename": output_filename})


@app.route('/progress')
def progress():
    try:
        with open(PROGRESS_FILE, 'r') as f:
            return jsonify(json.load(f))
    except FileNotFoundError:
        return jsonify({"progress": 0.0, "filename": ""})


@app.route('/uploads/<path:filename>')
def download(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
