from flask import Flask, render_template, request, jsonify
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.json['image']
    header, encoded = data.split(",", 1)
    image_data = base64.b64decode(encoded)
    image = Image.open(BytesIO(image_data))
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    buffered = BytesIO()
    flipped_image.save(buffered, format="PNG")
    flipped_image_data = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return jsonify({'flipped_image': f'data:image/png;base64,{flipped_image_data}'})

if __name__ == '__main__':
    app.run()
