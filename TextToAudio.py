from gtts import gTTS
import playsound

texto = "Ya puedes retirar tu producto de la bandeja"

# Crear objeto gTTS
tts = gTTS(text=texto, lang='es')

# Guardar archivo de audio
tts.save("audio.mp3")

#Reproducir archivo de audio
playsound.playsound('audio.mp3')
