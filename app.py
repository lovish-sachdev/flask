from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import base64
from PIL import Image
from io import BytesIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('image')
def handle_image(data):
    header, encoded = data.split(",", 1)
    image_data = base64.b64decode(encoded)
    image = Image.open(BytesIO(image_data))
    flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
    buffered = BytesIO()
    flipped_image.save(buffered, format="PNG")
    flipped_image_data = base64.b64encode(buffered.getvalue()).decode('utf-8')
    emit('flipped_image', f'data:image/png;base64,{flipped_image_data}')

if __name__ == '__main__':
    socketio.run(app)
