class Book:

    def __init__(self, title, author):  # Título, Autor
        self.__title = title
        self.author = author

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title


book_01 = Book('Python course', 'Alcimar Costa')  # Curso de Python
print(book_01.author)

book_01.author = 'José da Silva'
print(book_01.title)

book_01.title = 'New author'  # Novo autor
print(book_01.title)
