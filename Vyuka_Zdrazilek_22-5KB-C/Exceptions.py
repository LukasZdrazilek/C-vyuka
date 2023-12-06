import logging

# Configure logging
logging.basicConfig(filename='error_logs.txt', level=logging.ERROR)

while True:
    try:
        num1 = int(input("Zadejte prvni cislo: "))
        num2 = int(input("Zadejte druhe cislo: "))
        
        vysledek = num1 / num2
        print("Vysledek:", vysledek)
        break
        
    except ValueError as e:
        logging.error("Error: Neni integer - %s", e)
        print("Error: Prosim zadejte integer")
        
    except ZeroDivisionError as e:
        logging.error("Error: Deleni nulou - %s", e)
        print("Error: Nelze delit nulou")