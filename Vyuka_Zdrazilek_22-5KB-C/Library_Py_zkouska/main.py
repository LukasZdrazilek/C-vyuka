from book import Book 
from library import Library 

def main(): 

    book = Book("10;Animal Farm;Orwell George;Available") 

    print(book) 
    print() 

    library = Library("Vyuka_Zdrazilek_22-5KB-C/Library_Py_zkouska/data.txt")
# nevim jestli je to spravna cesta tady na githubu, nejede mi tu python, ale v mem vscode to vse funguje

    print(library) 
    print() 

    library.add_book(book) 
    print() 

    book.set_id(library.get_unique_id()) 

    library.add_book(book) 
    print() 
    print("Dostupné knihy:") 

    library.show_available_books() 
    print() 

    print("Půjčení knihy:") 
    library.find_book_and_borrow_it("Kill") 
    print() 

    library.find_book_and_borrow_it("a") 
    print() 
    
    library.find_book_and_borrow_it("Great") 
    print() 

    print("Dostupné knihy:") 
    library.show_available_books() 
    print() 
 
if __name__ == "__main__": 

    main()