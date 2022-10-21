import machine
from time import sleep
from config import *

while True:
    cmd = input("(1) - Write in Shell\n(2) - Read from File\n\n")

    if cmd == "1":
        text = input("\n: ")
        break
    elif cmd == "2":
        path = input("\nPath: ")
        # Opens file path -> defines text as file text -> breaks out | on OSError -> prints invalid path -> loops back to input
        try:
            f = open(path, "r")
            text = f.readline()
            break
        except OSError:
            print(f"\nInvalid path '{path}'\n")
    else:
        print(f"\nInvalid input '{cmd}'\n")
   
   
morse = ""

# Encoder, for key in dict -> replaces char with dict value -> if char isn't equal to space -> prints char
for char in text:
    for key in dict.keys():
        char = char.upper().replace(key, dict[key])
    sleep(char_wait)
    if char != ' ':
        print(f"\n{rev_dict[char]}")
    # Interpreter, for signal (+ -) in char -> prints char -> if signal equals - or + -> turns on led and sleeps | sleeps -> turns of led
    for signal in char:
        print(signal)
        if signal == "-":
            led.value(1)
            sleep(short)
        elif signal == "+":
            led.value(1)
            sleep(long)
        elif signal == " ":
            sleep(space)
        led.value(0)
        sleep(signal_wait)
        
