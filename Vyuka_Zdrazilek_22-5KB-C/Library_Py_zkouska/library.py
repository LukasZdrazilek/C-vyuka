from book import Book

class Library:
             
    def __init__(self, path_to_file):           # konstruktor naplní knihy z .txt do kolekce
        self.path = path_to_file
        self.books = []
        with open(self.path, 'r') as file:
            for line in file:
                line = line.rstrip()
                book_info = line.strip().split(';')
                print(book_info)
                if len(book_info) == 4:
                    book = Book(';'.join(book_info))
                    self.books.append(book)
                else:
                    print(f"Issue with data format in line: {line}")
            
    
    def add_book(self, book):           # přidá knihu do kolekce za předpokladu, že v systému již neexistuje kniha se stejným ID
        for i in self.books:
            if i.id == book.id:
                return
        self.books.append(book)
        
    
    def get_unique_id(self) -> int:                      # vrátí kladné ID, které nebylo v systému ještě použito
        used_ids = [book.id for book in self.books]
        unique_id = 1
        while unique_id in used_ids:
            unique_id += 1
        return unique_id
        
    
    def show_available_books(self):    # vypíše všechny dostupné knihy
        for book in self.books:
            if book.is_available():
                print(book)
        
    
    def __repr__(self):                    # vrací všechny knihy ve fromátu string kniha na každém řádku
        for book in self.books:
            print(str(book))
           
    def find_book_and_borrow_it(self, name):
        found_books = []
        for book in self.books:
            if name.lower() in book.name.lower():
                found_books.append(book)

        if len(found_books) == 0:
            print("No such book in library")
        elif len(found_books) == 1:
            print(found_books[0])
            borrow = input("Do you want to borrow this book? (yes/no): ")
            if borrow.lower() == "yes":
                found_books[0].borrow_book()
        else:
            print("Multiple books found:")
            for book in found_books:
                print(book)
    
    # najde knihu podle jména, nebo jeho části. Pokud najde více knih vytiskne je. Pokud nenajde žádnou informuje uživatele. 
    # Pokud najde právě jednu, vypíše ji a zeptá se, zdali si ji chce uživatel půjčit. Pokud ano změní její dostupnost.   
    
    def __str__(self):
        return '\n'.join(str(book) for book in self.books)
        