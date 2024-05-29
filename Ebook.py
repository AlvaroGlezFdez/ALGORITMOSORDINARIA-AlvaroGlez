from Genre import GENRE
from datetime import date
from Book import Book





class EBook(Book):
    def __init__(self,id,title,author,pages,publication_date,genres,format):
      super().__init__(id,title,author,pages,publication_date,genres)
      self.format = format

    def get_format(self):
        return self.format
    
    def __str__(self):
        return f"{self.author} escribió {self.title} con {self.pages} páginas en formato {self.format}"
  
    


def main():
   

    print("=================================================================.")
    print("Test Case 1: Create an EBook.")
    print("=================================================================.")
    ebook = EBook(1, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY], "EPUB.")

    if ebook.get_id() == 1:
        print("Test PASS. The parameter id has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if ebook.get_title() == "Harry Potter":
        print("Test PASS. The parameter title has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if ebook.get_author() == "J.K. Rowling":
        print("Test PASS. The parameter author has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if ebook.get_pages() == 345:
        print("Test PASS. The parameter pages has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if ebook.get_publication_date() == date.today():
        print("Test PASS. The parameter publication_date has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if ebook.get_genres() == [GENRE.FANTASY]:
        print("Test PASS. The parameter genres has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if ebook.get_format() == "EPUB.":
        print("Test PASS. The parameter format has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    ebook2 = EBook(2, "Harry Potter", "J.K. Rowling", 345, date.today(), [GENRE.FANTASY], "EPUB.")

    if str(ebook2) == "J.K. Rowling escribió Harry Potter con 345 páginas en formato EPUB.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
        print(str(ebook2))
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(ebook2))


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()