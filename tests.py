from main import BooksCollector
import pytest

class TestBooksCollector:


##################### 1. Тест структуры __init__ #####################
    def test_init_(self):
        collector = BooksCollector()
        collector.books_genre['Мамочки'] = 'Детектив'
        collector.favorites.append('Мамочки')
        assert (((len(collector.books_genre) == 1
                and len(collector.favorites) == 1)
                and len(collector.genre) == 5)
                and len(collector.genre_age_rating) == 2)

##################### 2. Тест добавление 2-ух книг add_new_book #####################
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

##################### 3. Тест добавление жанра книге set_book_genre #####################
    def test_set_book_genre_add_book(self):
        collector = BooksCollector()
        collector.books_genre['Гордость и предубеждение и зомби'] = ''
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert (collector.books_genre['Гордость и предубеждение и зомби'] == 'Ужасы')

##################### 4. Тест получение жанра книги get.book.genre #####################
    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.books_genre['Гордость и предубеждение и зомби'] = 'Ужасы'
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Ужасы'

##################### 5. Тест получение книг по жанру get_books_with_specific_genre #####################
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.books_genre['Гордость и предубеждение и зомби'] = 'Ужасы'
        collector.books_genre['Астрал'] = 'Ужасы'
        collector.books_genre['Папочки'] = 'Комедии'
        collector.books_genre['Мамочки'] = 'Детективы'
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2

##################### 6. Тест получение словаря get_books_genre #####################
    @pytest.mark.parametrize('name, book_genre',
                             [
                                 ['Гордость и предубеждение и зомби', 'Ужасы'],
                                 ['Папочки', 'Комедии'],
                                 ['Мамочки', 'Детективы']
                             ]
                             )
    def test_get_books_genre_three_books(self, name, book_genre):
        collector = BooksCollector()
        collector.books_genre['Гордость и предубеждение и зомби'] = 'Ужасы'
        collector.books_genre['Папочки'] = 'Комедии'
        collector.books_genre['Мамочки'] = 'Детективы'
        assert ((collector.get_books_genre())[name] == book_genre)

##################### 7. Тест получение книг для детей get_books_for_children #####################
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.books_genre['Гордость и предубеждение и зомби'] = 'Ужасы'
        collector.books_genre['Папочки'] = 'Комедии'
        assert len(collector.get_books_for_children()) == 1

##################### 8. Тест добавления книги в избранное add_book_in_favorites #####################
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.books_genre['Гордость и предубеждение и зомби'] = 'Ужасы'
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.favorites

##################### 9. Тест удаление книги из избранного delete_book_from_favorites #####################
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.favorites.append('Мамочки')
        collector.delete_book_from_favorites('Мамочки')
        assert 'Мамочки' not in collector.favorites

##################### 10. Тест удаление книги из избранного delete_book_from_favorites #####################
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.favorites.append('Мамочки')
        collector.favorites.append('Папочки')
        assert len(collector.get_list_of_favorites_books()) == 2
