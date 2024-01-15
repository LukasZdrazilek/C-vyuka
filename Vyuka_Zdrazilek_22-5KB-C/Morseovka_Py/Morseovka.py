def morseovka_nacitani(file_path):
    morseovka = {}
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                elements = line.strip().split(' ', 1)
                if len(elements) == 2:
                    character, code = elements
                    morseovka[character] = code

    return morseovka


def prekladac(input_text, morseovka_nactena):
    morseovka = [morseovka_nactena.get(char.upper(), char) for char in input_text]
    return ' '.join(morseovka)

def main():
    file_path = 'Morseovka_Py/morseovka.txt'
    morseovka_nactena = morseovka_nacitani(file_path)

    user_input = input("Zadejte slovo nebo vetu: ")
    vysledek = prekladac(user_input, morseovka_nactena)

    print("Morseovkou:", vysledek)

if __name__ == "__main__":
    main()
