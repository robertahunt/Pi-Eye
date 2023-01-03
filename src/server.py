import time
import logging
from bottle import route, run
from logging import handlers
from picamera2 import Picamera2, Preview

global picam2
try:
    picam2 = Picamera2()
    picam2.start()
except:
    pass

class PiEye():
    def __init__(self, debug=False):
        self.logger = self.make_logger(debug)
        pass
    
    def make_logger(self, debug):
        log_level = logging.DEBUG if debug else logging.INFO
        
        logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
        logger = logging.getLogger()

        fileHandler = logging.handlers.RotatingFileHandler('/home/pi/pieye.log', maxBytes=(1048576*5), backupCount=7)
        fileHandler.setFormatter(logFormatter)
        logger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        logger.addHandler(consoleHandler)
        
        return logger
        
    def reinit_camera(self):
        try:
            if hasattr(self, 'camera'):
                self.camera.stop()
                
            self.logger.debug('Trying to access Camera...')
            self.camera = Picamera2()
            
            self.logger.debug('Setting up configuration..')
            self.preview_config = self.camera.create_preview_configuration(queue=False)
            self.image_config = self.camera.create_still_configuration(losres={"size":(320,240)},display='lores',queue=False)
            
            # ensures sizes match sensor sizes and speeds up capture
            self.camera.align_configuration(self.image_config)
            self.camera.configure(self.image_config)
            self.logger.debug('Done getting camera ready')
            
            return True
        except Exception:
            self.logger.info('Could not connect to camera')
            return False

    def check_camera_is_setup(self):
        self.logger.debug('Checking if already set up camera')
        if hasattr(self, 'camera'):
            return True
        else:
            return self.reinit_camera()
        
    def capture_preview(self):
        self.check_camera_is_setup()
        self.logger.debug('Roberta should implement this')
        return [[None]]
    
    def capture_image(self):
        self.check_camera_is_setup()
        self.logger.debug('Roberta should implement this')
        return [[None]]
        

pieye = PiEye()

@route('/reinitCamera')
def reinit_camera():
    pieye.reinit_camera()

@route('/getPreview')
def get_preview():
    arr = pieye.capture_preview()
    return {'image':str(arr[0][0])}

@route('/takeImage')
def take_image():
    return {}

@route('/getImage')
def get_image():
    
    
    arr = pieye.capture_image()
    return {'image':str(arr[0][0])}

@route('/takeAndGetImage')
def get_image():
    
    
    arr = pieye.capture_image()
    return {'image':str(arr[0][0])}

@route('/hello')
def hello():
    return "Hello World!"

run(host='pieyene.local', port=8080, debug=True)
