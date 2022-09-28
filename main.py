import machine
from time import sleep

text = input(": ")
morse = ""

for char in text:
    for key in dict.keys():
        char = char.upper().replace(key, dict[key])
    sleep(letter_wait)
    if char != ' ':
        print(f"\n{rev_dict[char]}")
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
