# Importar las librerías
import RPi.GPIO as GPIO
import time

# Configurar el modo de numeración de pines GPIO
GPIO.setmode(GPIO.BOARD)

# Configurar el pin 11 como una salida, y configurar la
# variable servo1 como pin 11 como PWM

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # OJO, el número 11 es el pin,
                         # y el 50 es el pulso = 50Hz pulse

#Inicializar el Modulador de Pulsos (PWM) para que empiece
# a correr, pero con el valor inicial de 0 (pulso apagado)

servo1.start(0)
servo1.ChangeDutyCycle(7) # Mueve el servo a 90 grados 
time.sleep(2) # Tiempo de espera de 2 segundos

servo1.ChangeDutyCycle(2) # Mueve el servo a 0 grados
time.sleep(2) # Tiempo de espera de 2 segundos

servo1.stop() # Detener el servo 
GPIO.cleanup() # Limpieza de señales en los pines
