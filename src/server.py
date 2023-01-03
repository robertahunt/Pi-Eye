from bottle import run
from routes import *

run(host="pieyene.local", port=8080, debug=True, reloader=True)
