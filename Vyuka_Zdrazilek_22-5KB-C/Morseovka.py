
def translateToMorseCode(txt):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-','Y': '-.--', 'Z': '--..', ' ': '-.-.-.-', ',': '--..--', ':': '---...', 
        ';': '-.-.-.', '.': '.-.-.-', '"': '.-..-.', '(': '-----.', ')': '.-----', '\'': '-.--.-', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}

    with open(txt, "r") as file:
        for line in file:
            line = line.strip().upper()     # 
            for char in line:
                if char in morse_code:
                    print(morse_code[char], end=' ')
                else:
                    print(char)
            print("")

translateToMorseCode("morseovka.txt")