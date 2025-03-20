import pandas as pd
import numpy as np

class BookLover:
    
    def __init__(self, name, email, fav_genre, *num_books, **book_list):
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        self.name = name
        self.email = email
        self.fav_genre = fav_genre

    def add_book(self, book_name, rating):
        if self.has_read(book_name):
            return False

        else: # adds book to dataframe if book is not already in the list
            new_book = pd.DataFrame({
                "book_name": [book_name],
                "book_rating": [rating]
            })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
            
    
    def has_read(self, book_name):
        return any(self.book_list.book_name == book_name)
        
    def num_books_read(self):
        return len(self.book_list)
    
    def fav_books(self):
        return self.book_list[self.book_list["book_rating"] > 3]