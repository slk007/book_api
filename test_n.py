from home import GoodreadsAPIClient, myException
import config
import unittest

dev_key = config.developer_key

class NegativeTest(unittest.TestCase):

    def setUp(self):

        self.obj = GoodreadsAPIClient()
        self.obj.input_url = "https://www.gooreads.com/book/show/22034.The_Godfather"

    def test_get_book_id_from_input_url(self):

        with self.assertRaises(myException):
            self.obj.get_book_id_from_input_url()



if __name__ == "__main__":
    unittest.main()
