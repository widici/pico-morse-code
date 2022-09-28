import machine
from time import sleep
led=machine.Pin(25, machine.Pin.OUT)

short=0.1
long=short*4
space=0.75
symbol_wait=0.25
letter_wait=symbol_wait*2

dict = {'A': '-+', 'B': '+---',
        'C': '+-+-', 'D': '+--', 'E': '-',
        'F': '--+-', 'G': '++-', 'H': '----',
        'I': '--', 'J': '-+++', 'K': '+-+',
        'L': '-+--', 'M': '++', 'N': '+-',
        'O': '+++', 'P': '-++-', 'Q': '++-+',
        'R': '-+-', 'S': '---', 'T': '+',
        'U': '--+', 'V': '---+', 'W': '-++',
        'X': '+--+', 'Y': '+-++', 'Z': '++--',
        '1': '-++++', '2': '--+++', '3': '---++',
        '4': '----+', '5': '-----', '6': '+----',
        '7': '++---', '8': '+++--', '9': '++++-',
        '0': '+++++', ', ': '++--++','?': '--++--',
        '/': '+--+-', '(': '+-++-', ')': '+-++-+'
}

rev_dict = {v: k for k, v in dict.items()}

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
