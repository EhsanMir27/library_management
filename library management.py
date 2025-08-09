class Library:
        def __init__(self,books,borrowed):
            self.books = books
            self.borrowed = borrowed


        def search(self, name):
            return name in self.books

        def borrow(self, name):
            if name in self.books and name not in self.borrowed:
                self.borrowed.append(name)
                self.books.remove(name)
                return True
            else:
                return False

        def return_book(self, name):
            if name in self.borrowed:
                self.borrowed.remove(name)
                self.books.append(name)
                return True
            else :
                return False

lib = Library(books=["book1", "book2", "book3","book4","book5"],borrowed=[])

while True:
    user_choice=input('choose an option\n1.search\n2.borrow\n3.return\n4.exit\n-> ')
    if user_choice=='1':
        user_search=input('search for a book :')
        if lib.search(user_search):
            pass
        else:
            print('out of order')
    elif user_choice=='2':
        print(lib.books)
        user_borrow=input('choose a book to borrow :')
        if lib.borrow(user_borrow) :
            print(f"'{user_borrow}' borrowed successfully.")
        else:
            pass

    elif user_choice=='3':
        print(lib.borrowed)
        user_return=input('return a book : ')
        if lib.return_book(user_return):
            print(f"'{user_return}' returned successfully.")
    elif user_choice=='4':
        break

