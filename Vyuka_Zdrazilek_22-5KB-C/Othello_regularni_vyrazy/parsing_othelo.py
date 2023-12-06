import requests
import re
from os.path import join, realpath, dirname, exists

if not exists(join(dirname(realpath(__file__)), "Othello.txt")):
    resp = requests.get("https://www.gutenberg.org/cache/epub/2267/pg2267.txt")
    if resp.ok:
        with open(join(dirname(realpath(__file__)),"Othello.txt"), "x", encoding = resp.apparent_encoding) as file:
            file.write(resp.text)
            
with open(join(dirname(realpath(__file__)), "Othello.txt"), "r") as file:
    book = file.read()
    
    slova = re.findall(r"[A-Za-z]+", book)      # set. misto re. pro unikatni slova
    
    # Hledani poctu unikatnich slov a vypsani 10 nejvice vyskytovanych
    slova_unikat = {slovo:slova.count(slovo) for slovo in set(slova)}
    print(sorted(slova_unikat.items(), key = lambda x : x[1], reverse = True)[:10])
    
    
    vety = re.findall(r"[^.!?]+[.!?]", book)
    average_length = sum(len(veta) for veta in vety) / len(vety)
    print("Pocet vet:", len(vety))
    print("Prumerna delka vety:", average_length)
