from flask import Flask, request
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from predict import predict_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def home():
    return '''
    <h2>Upload File Scanner</h2>

    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Scan File">
    </form>
    '''


@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(path)

    prediction, details = predict_file(path)

    result_html = ""

    if prediction == "MALICIOUS":
        result_html = "<h3 style='color:red'>❌ Malicious file detected</h3>"
    else:
        result_html = "<h3 style='color:green'>✅ File is safe</h3>"

    return f'''
    <h2>Upload File Scanner</h2>

    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Scan File">
    </form>

    <hr>

    {result_html}

    <h4>Analysis Details</h4>

    <p>File Size: {details["file_size"]}</p>
    <p>Entropy: {details["entropy"]:.2f}</p>
    <p>Pattern Score: {details["pattern_score"]}</p>
    <p>Magic Mismatch: {details["magic_mismatch"]}</p>
    '''


app.run(host="0.0.0.0", port=5000)
