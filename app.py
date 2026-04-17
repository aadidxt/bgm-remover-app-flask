<<<<<<< HEAD
from flask import Flask, request, send_file
from rembg import remove
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    if "image" not in request.files:
        return {"error": "No file uploaded"}, 400

    file = request.files["image"]
    input_bytes = file.read()

    output_bytes = remove(input_bytes)

    return send_file(
        io.BytesIO(output_bytes),
        mimetype="image/png"
    )

if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask, request, send_file
from rembg import remove
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    if "image" not in request.files:
        return {"error": "No file uploaded"}, 400

    file = request.files["image"]
    input_bytes = file.read()

    output_bytes = remove(input_bytes)

    return send_file(
        io.BytesIO(output_bytes),
        mimetype="image/png"
    )

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 00d15a2b9085af9c56f62f96919ce60b289e38aa
