import machine
led=machine.Pin(25, machine.Pin.OUT)

short=0.1 # Wait time on -
long=short*4 # Wait time on +
space=0.75 # Wait time on space
signal_wait=0.25 # Wait time between signals
char_wait=signal_wait*2 # Wait time between characters

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

rev_dict = {v: k for k, v in dict.items()} # Key, value -> value, key
