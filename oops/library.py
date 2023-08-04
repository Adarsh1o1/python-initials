class library:
    def __init__(self) -> None:
        self.number = 0
        self.books = []

    def add_books(self, book):
        self.books.append(book)
        self.number = self.books.__len__()

    def checker(self):
        if self.number == len(self.books):
            print("Program is working FINE.")
            # print(self.books.__len__())
            # print(self.number)
        else:
            print("Program is Faulty.")

    def show_info(self):
        print(f"The library has {self.number} books")

    def print_books(self):
        for i in self.books:
            print(i)

    @staticmethod #static method helps up to create a method without self key word
    def adarsh(a,b):
        return a+b



book = library()
book.add_books("let us see1")
book.add_books("let us see2")
book.add_books("let us see3")
book.checker()
book.show_info()
book.print_books()


class movies(library):
    def show_movies(self):
        print("gg")


muvi = movies()
muvi.add_books("hera feri")
muvi.add_books("hera feri")
muvi.add_books("hera feri")
muvi.add_books("hera feri")
muvi.add_books("hera feri")
muvi.print_books()
