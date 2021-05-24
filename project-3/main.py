class Library:

    def __init__(self, listofbooks):
        self.books = listofbooks

    def display(self):
        print('Books present in the li. :')
        for books in self.books:
            print('\t *' + str(books))

    def borrow(self, borrow):
        if borrow in self.books:
            print(f'You have been issued the book {borrow}\nPlease keep it safe')
            self.books.remove(borrow)
            return True

        else:
            print('The book is not available')
            return False

    def returnbooks(self, BookName):
        print(f'Thanks for return the book {BookName}. Have a good day')
        self.books.append(BookName)


class Student:
    def request(self):
        self.book = input('Enter the name of the book that you want to borrow: ')
        return self.book

    def returnb(self):
        self.book = input('Enter the name of the book that you want to return: ')


if __name__ == '__main__':
    main = Library(['django', 'c++', 'c', 'python'])
    student = Student()
    while True:
        try:
            welcome = '''========Welcome to the central library========
            Please choose an option
            1. Listing all the books 
            2. Request a book
            3. Return a book
            4. Exit
            '''
            print(welcome)
            ask = int(input('Enter your chose: '))
            if ask == 1:
                main.display()
            elif ask == 2:
                main.borrow(student.request())
            elif ask == 3:
                main.returnbooks(student.returnb())
            elif ask == 4:
                print('Thanks for using the library :)\nHave a good day\n==================>\n\tShajidur Rahman\n:-) :) :)')
                exit()
        except Exception:
            print('make sure enter a number :(')

