from flask import Flask, render_template_string, request   # Importing the Flask modules 
import RPi.GPIO as GPIO     # Importing the GPIO library 
from time import sleep      # Import sleep module from time library 
servo_pin = 11 # GPIO Pin where servo is connected
GPIO.setmode(GPIO.BOARD)      # Define the Pin numbering type. Here we are using BCM type
# Defing Servo Pin as output pin
GPIO.setup(11, GPIO.OUT)     
p = GPIO.PWM(11, 50)  # PWM channel at 50 Hz frequency
p.start(0) # Zero duty cycle initially
app = Flask(__name__)
#HTML Code 
TPL = '''
<html>
     <img src="https://e7.pngegg.com/pngimages/939/985/png-clipart-gray-robot-cute-robot-model-robot-s-computer-wallpaper-cartoon-thumbnail.png" alt="">
    <head><title>Web Page Controlled Servo</title></head>
    <body>
    <h2> Web Page to Control Servo</h2>
        <form method="POST" action="test">
            <h3> Use the slider to rotate servo  </h3>
            <p>Slider   <input type="range" min="1" max="12.5" name="slider" /> </p>
            <input type="submit" value="submit" />
        </form>
    </body>
</html>

'''
@app.route("/")
def home():                                                                                                                                                         
    return render_template_string(TPL)                        
@app.route("/test", methods=["POST"])
def test():
    # Get slider Values
    slider = request.form["slider"]
    # Change duty cycle
    p.ChangeDutyCycle(float(slider))
    sleep(1)
    # Pause the servo
    p.ChangeDutyCycle(0)
    return render_template_string(TPL)
# Run the app on the local development server
if __name__ == "__main__":
    app.run()