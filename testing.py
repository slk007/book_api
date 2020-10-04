from home import GoodreadsAPIClient
import config
import unittest

dev_key = config.developer_key

class SimpleTest(unittest.TestCase):

    def setUp(self):

        self.obj = GoodreadsAPIClient()
        self.obj.input_url = "https://www.goodreads.com/book/show/12177850-a-song-of-ice-and-fire"

    def test_get_book_id_from_input_url(self):

        self.obj.get_book_id_from_input_url()
        book_id = self.obj.book_id

        self.assertEqual(book_id, '12177850')

    def test_make_book_api_url(self):

        url = "https://www.goodreads.com/book/show/12177850.xml?key="+ dev_key

        self.obj.make_book_api_url()
        book_url = self.obj.book_url
        print(book_url, url)
        self.assertEqual(book_url, url)

    def test_get_book_details(self):

        self.obj.get_book_details()

        self.assertEqual(self.obj.book_details['title'], "A Song of Ice and Fire (A Song of Ice and Fire, #1-5)")
        self.assertEqual(self.obj.book_details['publication_year'], "2011")
        self.assertEqual(self.obj.book_details['num_pages'], "5216")
        self.assertEqual(self.obj.book_details['authors'], "George R.R. Martin")


if __name__ == "__main__":
    unittest.main()