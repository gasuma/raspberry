# Importar las librerías
import RPi.GPIO as GPIO
import time
import tkinter as tk # Importar el módulo tkinter y crear el objeto tk

def button1_click(): # Definir la función del primer boton "button1click"
    print("Abrir")   # imprimir en la consola la palabra "Abrir"
    servo1.start(0)  #Inicializar el Modulador de Pulsos (PWM) para que empiece
                     # a correr, pero con el valor inicial de 0 (pulso apagado) 
    
    servo1.ChangeDutyCycle(7) # Mueve el servo a 90 grados

def button2_click(): # Definir la función del primer boton "button1click"
    print("Cerrar")  # imprimir en la consola la palabra "Abrir"
    servo1.ChangeDutyCycle(2) # Mueve el servo a su posición inicial (0 grados)
    
GPIO.setmode(GPIO.BOARD) # Configurar el modo de numeración de pines GPIO

# Configurar el pin 11 como una salida, y configurar la
# variable servo1 como pin 11 como PWM

GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # OJO, el número 11 es el pin,
                         # y el 50 es el pulso = 50Hz pulse


# Luego creamos dos objetos Botón, pasando la ventana root como primer argumento
# y el texto para mostrar en el botón como argumento de texto.
# Finalmente, llamamos al método pack() en cada botón para agregarlos a la
# ventana.
root = tk.Tk()

button1 = tk.Button(root, text="Abriendo", command=button1_click)
button1.pack() 

button2 = tk.Button(root, text="Cerrando", command=button2_click)
button2.pack()

root.mainloop() # Se llama al método mainloop() en el objeto Tk para iniciar
                # el bucle de eventos y mostrar la ventana con los botones.
quit() # El programa termina con código de salida 0