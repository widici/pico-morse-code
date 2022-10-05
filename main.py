import machine
from time import sleep
from config import *

text = input(": ")
morse = ""

# Encoder, for key in dict -> replaces char with dict value -> if char isn't equal to space -> prints char
for char in text:
    for key in dict.keys():
        char = char.upper().replace(key, dict[key])
    sleep(letter_wait)
    if char != ' ':
        print(f"\n{rev_dict[char]}")
    # Interpreter, for signal (+ -) in char -> prints char -> if signal equals - or + -> turns on led and sleeps | sleeps -> turns off led
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
        sleep(symbol_wait)
        
