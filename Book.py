from datetime import date
from Genre import GENRE
class Book:
    def __init__(self, id, title, author, pages, publication_date, genres=[]):
        self.id = id
        self.title = title
        self.author = author
        self.pages = pages
        self.publication_date = publication_date
        self.genres = genres
      
        if not isinstance(id, int) or id <= 0:
            raise ValueError("ID debe ser un entero positivo.")
        
        if not isinstance(title, str) or not title:
            raise ValueError("Título debe ser una cadena no vacía.")
        
        if not isinstance(author, str) or not author:
            raise ValueError("Autor debe ser una cadena no vacía.")
        
        if not isinstance(pages, int) or pages <= 1:
            raise ValueError("Número de páginas debe ser un entero mayor que 1.")
        
        if not isinstance(publication_date, date) or publication_date > date.today():
            raise ValueError("La fecha de publicación no puede ser una fecha futura.")

        if not isinstance(genres, list):
            raise ValueError("Géneros debe ser una lista.")
        
        for genre in genres:
            if not isinstance(genre, GENRE):
                raise ValueError("Cada género debe ser un valor de la enumeración GENRE.")
        
        if len(set(genres)) != len(genres):
            raise ValueError("No pueden haber géneros repetidos.")

    # Getters y Setters
    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_pages(self):
        return self.pages
    
    def get_publication_date(self):
        return self.publication_date
  
    def get_genres(self):
        return self.genres
  
    def add_genre(self, genre):
        if genre not in self.genres:
            self.genres.append(genre)

    # Método para comparar si dos libros son iguales basados en el identificador único
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.id == other.get_id()
        return False

    # Método para representar el libro de forma legible
    def __str__(self):
        return f"{self.author} escribió {self.title} con {self.pages} páginas."
    
    
    
    
    
def main():
    
    
    
    print("=================================================================.")
    print("Test Case 1: Create a Book.")
    print("=================================================================.")
    book = Book(1, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])

    if book.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_title() == "Harry Potter":
        print("Test PASS. The parameter title has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_author() == "J.K. Rowling":
        print("Test PASS. The parameter author has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_pages() == 345:
        print("Test PASS. The parameter pages has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_publication_date() == date.today():
        print("Test PASS. The parameter publication_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if book.get_genres() == [GENRE.FANTASY]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    book2 = Book(2, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])

    if str(book2) == "J.K. Rowling escribió Harry Potter con 345 páginas.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(book2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(book2))


    print("=================================================================.")
    print("Test Case 3: book add_genre")
    print("=================================================================.")
    book2.add_genre(GENRE.FICTION)
    genres = book2.get_genres()
    if genres == [GENRE.FANTASY, GENRE.FICTION]:
        print("Test PASS. The method add_genre(genre) has been implemented correctly.")
    else:
        print("Test FAIL. Check the method add_genre(genre), "+ " RESULT: " + str(genres))
    
    print("=================================================================.")
    print("Test Case 4: Test the method __eq__")
    print("=================================================================.")
    book3 = Book(2, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY])
    if book2 == book3:
        print("Test PASS. The method __eq__ has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __eq__().")

# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()
