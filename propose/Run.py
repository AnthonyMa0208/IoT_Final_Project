from flask import Flask
from flask import render_template, request
import RPi.GPIO as gpio
import time

app = Flask(__name__)

gpio.setmode(gpio.BCM)
gpio.setup(17,gpio.OUT)
gpio.setup(22,gpio.OUT)
gpio.setup(23,gpio.OUT)
gpio.setup(24,gpio.OUT)
gpio.setwarnings(False)
gpio.output(17,False)
gpio.output(22,False)
gpio.output(23,False)
gpio.output(24,False)
print ("DOne")


a=1
@app.route("/")
def index():
    return render_template('robot.html')

@app.route('/left_side')
def left_side():
   data1="LEFT"
   gpio.output(17,False)
   gpio.output(22,False)
   gpio.output(23,True)
   gpio.output(24,False)
   return 'true'

@app.route('/right_side')
def right_side():
   data1="RIGHT"
   gpio.output(17,False)
   gpio.output(22,True)
   gpio.output(23,False)
   gpio.output(24,False)
   return 'true'

@app.route('/up_side')
def up_side():
   data1="FORWARD"
   gpio.output(17,False)
   gpio.output(22,True)
   gpio.output(23,True)
   gpio.output(24,False)
   return 'true'

@app.route('/down_side')
def down_side():
   data1="BACK"
   gpio.output(17,True)
   gpio.output(22,False)
   gpio.output(23,False)
   gpio.output(24,True)
   return 'true'

@app.route('/stop')
def stop():
   gpio.output(17,False)
   gpio.output(22,False)
   gpio.output(23,False)
   gpio.output(24,False)
   return 'true'

if __name__ == "__main__":
 print ("Start")
 app.run(host='0.0.0.0',port=5010)

0