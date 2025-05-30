from main import BooksCollector
import pytest

class TestBooksCollector:

########################## 1. Тест добавление 2-ух книг add_new_book ##########################
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

########################## 2. Тест добавление жанра книге set_book_genre ##########################
    def test_set_book_genre_add_book(self):
        collector = BooksCollector()
        collector.books_genre['Гордость и предубеждение и зомби'] = ''
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert (collector.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы')

########################## 3. Тест получение жанра книги get.book.genre ##########################
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.books_genre['Гордость и предубеждение и зомби'] = 'Ужасы'
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

########################## 4. Тест получение книг по жанру get_books_with_specific_genre ##########################
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.books_genre['Гордость и предубеждение и зомби'] = 'Ужасы'
        collector.books_genre['Астрал'] = 'Ужасы'
        collector.books_genre['Папочки'] = 'Комедии'
        collector.books_genre['Мамочки'] = 'Детективы'
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2


