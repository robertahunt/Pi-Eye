from pieye import PiEye
from bottle import route, run, abort, error



eye = PiEye(debug=True)

@route("/reinitCamera")
def reinit_camera():
    eye.reinit_camera()
    return {"Initialization":"Successful"}


@route("/getPreview")
def get_preview():
    arr = eye.capture_preview()
    return {"image": str(arr[0][0])}


@route("/takeImage")
def take_image():
    return {}


@route("/getImage")
def get_image():

    arr = eye.capture_image()
    return {"image": str(arr[0][0])}


@route("/takeAndGetImage")
def take_and_get_image():
    arr = eye.capture_image()
    return {"image": str(arr[0][0])}


@route("/hello")
def hello():
    return "Hello World!"