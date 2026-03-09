from playsound3 import playsound
import time

sound = playsound('C:\\Users\\Shaur\\Desktop\\useful python\\Morse_Code_Generator\\Stay.mp3', block=False)
while sound.is_alive():
    print("Sound is still playing!")
    time.sleep(2)
    
    
# sound.stop()