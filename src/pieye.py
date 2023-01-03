import time
import logging
from logging import handlers
from picamera2 import Picamera2
from bottle import abort

class PiEye():
    def __init__(self, debug=False):
        self.logger = self.make_logger(debug)
        pass
    
    def make_logger(self, debug):
        log_level = logging.DEBUG if debug else logging.INFO
        
        logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
        logger = logging.getLogger()
        logger.setLevel(log_level)

        fileHandler = handlers.RotatingFileHandler('/home/pi/pieye.log', maxBytes=(1048576*5), backupCount=7)
        fileHandler.setFormatter(logFormatter)
        logger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        logger.addHandler(consoleHandler)
        
        return logger
        
    def reinit_camera(self):
        try:
            if hasattr(self, 'camera'):
                self.camera.close()
                del self.camera
            time.sleep(2)
            self.logger.debug('Trying to access Camera..')
            self.camera = Picamera2()
            
            self.logger.debug('Setting up configuration..')
            self.preview_config = self.camera.create_preview_configuration()
            self.image_config = self.camera.create_still_configuration(lores={"size":(320,240)},display='lores')
            
            # ensures sizes match sensor sizes and speeds up capture
            self.camera.align_configuration(self.image_config)
            self.camera.configure(self.image_config)
            self.camera.start()
            self.logger.debug('Done getting camera ready')
            
            return True
        except Exception as ex:
            self.logger.info('Could not connect to camera' + str(ex))
            abort(500, "Error when initializing or connecting to the HQ camera module. Probably the cables are slightly out of place. Please reconnect them")
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
        