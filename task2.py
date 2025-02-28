from abc import ABC, abstractmethod


class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title: str = title
        self.author: str = author
        self.year: int = year

    def info(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: int) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass


class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library: LibraryInterface = library

    def add_book(self, title: str, author: str, year: int) -> None:
        self.library.add_book(title, author, year)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()


class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, title: str, author: str, year: int) -> None:
        book: Book = Book(title, author, year)
        self.books.append(book)

    def remove_book(self, title: str) -> None:
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break

    def show_books(self) -> None:
        for book in self.books:
            print(book.info())


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                if not title:
                    print("Error: Book title cannot be empty")
                    continue

                author = input("Enter book author: ").strip()
                if not author:
                    print("Error: Author name cannot be empty")
                    continue

                try:
                    year = int(input("Enter book year: ").strip())
                    if year <= 0:
                        print("Error: Year must be a positive number")
                        continue
                except ValueError:
                    print("Error: Year must be a valid number")
                    continue

                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
