'''
A class is a structure that abstracts a set of objects with similar characteristics.

Uma classe é uma estrutura que abstrai um conjunto de objetos com características similares.
'''


class Book:

    def __init__(self,  title, author, publisher, isbn, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.isbn = isbn
        self.year = year

    def __str__(self):
        return 'Title: %s, Author: %s, Publisher: %s, ISBN: %s, Year: %s' % \
                (self.title, self.author, self.publisher, self.isbn, self.year)


Book_01 = Book('Python course in 6h', 'Alcimar Costa', 'Udemy', '878-98-9988-988-9', 2018)
# Curso de Python em 6h

print(Book_01)
print(Book_01.title)
print(Book_01.author)
print(Book_01.publisher)
print(Book_01.isbn)
print(Book_01.year)
