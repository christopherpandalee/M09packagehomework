import pandas as pd
import numpy as np
import unittest
from booktest import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        test1addbook = BookLover("Panda", "email@email.com", "nonfiction")
        test1addbook.add_book("Deadly Education", 5)
        added_book = "Deadly Education"
        self.assertTrue(test1addbook.has_read(added_book))
        
        
    def test_2_add_book(self):
        test2addbook = BookLover("Panda", "email@email.com", "fiction")
        test2addbook.add_book("Deadly Education", 5)
        test2addbook.add_book("Deadly Education", 5)
        num_books = len(test2addbook.book_list)
        test_assert = num_books == 1
        self.assertTrue(test_assert)
        
    
    def test_3_has_read(self):
        test3addbook = BookLover("Panda", "email@email.com", "fiction")
        test3addbook.add_book("Deadly Education", 5)
        read_book = "Deadly Education"
        self.assertTrue(test3addbook.has_read(read_book))
        
    def test_4_has_read(self):
        test4addbook = BookLover("Panda", "email@email.com", "fiction")
        test4addbook.add_book("Deadly Education", 5)
        has_not_read = "Moby Dick"
        self.assertFalse(test4addbook.has_read(has_not_read))
        
    def test_5_num_books_read(self):
        test5addbook = BookLover("Panda", "email@email.com", "fiction")
        test5addbook.add_book("Deadly Education", 5)
        test5addbook.add_book("Last Graduate", 5)
        test5addbook.add_book("Golden Enclaves", 5)
        test5addbook.add_book("Braiding Sweetgress", 4)
        num_books_exp = 4
        self.assertEqual(test5addbook.num_books_read(), num_books_exp)
        
    def test_6_fav_books(self):
        test6addbook = BookLover("Panda", "email@email.com", "fiction")
        test6addbook.add_book("Deadly Education", 5)
        test6addbook.add_book("Last Graduate", 5)
        test6addbook.add_book("Golden Enclaves", 5)
        test6addbook.add_book("Braiding Sweetgress", 4)
        test6addbook.add_book("Moby Dick", 1)
        test6addbook.add_book("Grapes of Wrath", 2)
        out_fav_books = sum(test6addbook.fav_books().book_rating > 3)
        exp_rating_truthvalue = len(test6addbook.fav_books())
        self.assertTrue(out_fav_books == exp_rating_truthvalue)
        
        
    
if __name__ == '__main__':
    unittest.main(verbosity = 3)