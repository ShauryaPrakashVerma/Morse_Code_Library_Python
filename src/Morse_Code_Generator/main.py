from playsound3 import playsound
import time
import json


sound = playsound('C:/Users/Shaur/Desktop/Morse_Code_Library_Python/Morse_Code_Generator/Stay.mp3', block=False)
while sound.is_alive():
    print("Sound is still playing!")
    time.sleep(2)



with open("Morse_Code_Generator/morse_map.json", "r") as file:
    morse_data = json.load(file)
    # print(morse_data)
    
    print(morse_data["letters"]["A"])
    
#-------------------------------------------------------------------------------------------------------------

def get_input(self):
    msg = input("Enter the message to be encoded: ") 
    
    
# sound.stop()