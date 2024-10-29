import cv2
import numpy as np
import requests
import threading
from flask import Flask, Response, render_template

app = Flask(__name__)

# Global variables
SNAPSHOT_URL = 'http://192.168.1.111:6688/snapshot.jpg'
video_feed_active = False

def fetch_snapshot():
    while video_feed_active:
        response = requests.get(SNAPSHOT_URL)
        img_array = np.array(bytearray(response.content), dtype=np.uint8)
        frame = cv2.imdecode(img_array, -1)
        yield frame

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    while video_feed_active:
        frame = fetch_snapshot()
        if frame is None:
            continue
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_feed')
def start_feed():
    global video_feed_active
    video_feed_active = True
    threading.Thread(target=fetch_snapshot).start()
    return 'Live feed started.'

@app.route('/stop_feed')
def stop_feed():
    global video_feed_active
    video_feed_active = False
    return 'Live feed stopped.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
