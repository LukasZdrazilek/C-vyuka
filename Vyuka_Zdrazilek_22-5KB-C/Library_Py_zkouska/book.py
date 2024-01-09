class Book:
    
    
        
    def __init__(self, book_info):  # inicializace knihy ze stringu o struktuře "id;name;author;available" 
        self.id = 0
        self.name = ""
        self.author = ""
        self.available = False

        book_info = book_info.split(';')
        self.id = int(book_info[0])
        self.name = book_info[1]
        self.author = book_info[2]
        if book_info[3] == "Available":
            self.available = True
    
    def __lt__(self, other) -> bool:        # true pokud je autor dříve v abecedě než autor other
        return self.author < other.author
        
    
    def __eq__(self, other) -> bool:    # true pokud jsou id stejná
        return self.id == other.id
        
    
    def repr(self) -> str:          # vrací string reprezentující knihy v následujícím formátu: id;name;author;available
        return f"{self.id};{self.name};{self.author};{self.available}"
    
    def __str__(self):              # vypis knihy
        return f"ID: {self.id}, Title: {self.name}, Author: {self.author}, Available: {'Yes' if self.available else 'No'}"
    
    def set_id(self, new_id):       # nastaveni id
        self.id = new_id
        
    def is_available(self):         # je kniha dostupna?
        return self.available
        