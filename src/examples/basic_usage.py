from Morse_Code_Generator.encoder import encode
from Morse_Code_Generator.utils import load_language

print("Testing language loading:")
print(load_language("english"))
print("-----------------------------------------------------------------------------------------------")
print(load_language("russian"))
print("-----------------------------------------------------------------------------------------------")
print(load_language())

print("\nTesting encoder:")
print(encode("SOS"))
print(encode("HELLO WORLD i am shaurya"))
print(encode("123"))