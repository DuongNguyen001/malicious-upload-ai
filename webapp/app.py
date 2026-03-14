from flask import Flask, request, render_template
import os
import sys

# cho phép import file từ folder ngoài
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from predict import predict_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# =========================
# Trang chủ
# =========================
@app.route("/")
def home():
    return render_template("index.html")


# =========================
# Upload file
# =========================
@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["file"]

    path = os.path.join(UPLOAD_FOLDER, file.filename)

    file.save(path)

    prediction, details = predict_file(path)

    return render_template(
        "result.html",
        result=prediction,
        details=details
    )


# =========================
# Run server
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
