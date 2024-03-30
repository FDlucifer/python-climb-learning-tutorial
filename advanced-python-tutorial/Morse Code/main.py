# pip install playsound

import time
from playsound import playsound

translate_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

message = "This is just a message"
message = " ".join(translate_dict[c] for c in message.upper())

def play_morse_code(message):
    for c in message:
        if c == ".":
            playsound("short.mp3")
        elif c == "-":
            playsound("long.mp3")
            time.sleep(0.3)
        elif c == "/" or c == " ":
            time.sleep(0.5)
        else:
            print("invalid character detected!")

print(message)
play_morse_code(message)

reverse_dict = {v: k for k, v in translate_dict.items()}
reverse_message = "".join(reverse_dict[c] for c in message.split(" "))
print(reverse_message)