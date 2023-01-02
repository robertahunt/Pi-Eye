import time
from bottle import route, run
from picamera2 import Picamera2, Preview

global picam2
try:
    picam2 = Picamera2()
    picam2.start()
except:
    pass

@route('/reinitCamera')
def reinit_camera():
    global picam2
    try:
        picam2.close()
    except:
        pass

    picam2 = Picamera2()
    #camera_config = picam2.create_still_configuration(raw={}, main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
    #picam2.configure(camera_config)
    picam2.start()

@route('/getPhoto')
def get_photo():
    arr = picam2.capture_image("lores")
    return {'photo':str(arr[0][0])}

@route('/hello')
def hello():
    return "Hello World!"

run(host='robopi.local', port=8080, debug=True)
