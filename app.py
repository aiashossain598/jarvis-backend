from flask import Flask, request, send_file
from flask_cors import CORS
import img2pdf
import io

app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['POST'])
def convert():
    if 'image' not in request.files:
        return "No file", 400
    img_file = request.files['image']
    pdf_bytes = img2pdf.convert(img_file.read())
    return send_file(io.BytesIO(pdf_bytes), mimetype='application/pdf', as_attachment=True, download_name='jarvis_output.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)