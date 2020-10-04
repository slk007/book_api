import requests
import re
import json
import xml.etree.ElementTree as ET
import config

# getting developer key from config.py file
dev_key = config.developer_key

class myException(Exception):
    pass

class GoodreadsAPIClient:
    """class to input the url and Output the details of a book using GOODREADS API"""

    def __init__(self):

        self.book_id = None
        self.book_url = None
        self.input_url = None
        self.book_details = {}
        self.key = dev_key


    def get_book_id_from_input_url(self):
        """function to extract book id from the input url"""

        if self.input_url[0:36] == "https://www.goodreads.com/book/show/":

            remaining_url = self.input_url[36:]
            word_list = re.split('[.-]' ,remaining_url)

            if word_list[0].isnumeric():
                self.book_id = word_list[0]
            else:
                # raise the exception when book id is not found in the URL
                raise myException("InvalidGoodreadsURL")
        else:
            # raise exception when the first half of the URL does not match the req
            raise myException("InvalidGoodreadsURL")


    def input_url_from_user(self):
        """function to get input from user"""

        self.input_url = input("Input: ")
        if self.input_url[0] == '"' and self.input_url[-1] == '"':
            self.input_url = self.input_url[1:-1]



    def make_book_api_url(self):
        """use book id and developer key to make API link"""

        # format API_LINK = "https://www.goodreads.com/book/show/<book id>.xml?key=<your dev key>"

        self.book_url = f"https://www.goodreads.com/book/show/{self.book_id}.xml?key={self.key}"


    def get_book_details(self):
        """takes a Goodreads URL string as input and returns out information of the book"""

        try:
            # gives response for the request from the API url
            response = requests.get(self.book_url)

            # using ElementTree to store the response content in a tree
            root = ET.fromstring(response.content)
            book = root.find('book')

            # getting the required details
            self.book_details["title"] = book.find('title').text
            self.book_details["average_rating"] = book.find('average_rating').text
            self.book_details["ratings_count"] = book.find('ratings_count').text
            self.book_details["num_pages"] = book.find('num_pages').text
            self.book_details["image_url"] = book.find('image_url').text
            self.book_details["publication_year"] = book.find('publication_year').text

            # getting list of all the authors
            authors = book.find('authors')
            if authors:
                author_names_list = []
                for author in authors.iter('author'):
                    author_names_list.append(author.find('name').text)
                author_names_sentence = ", ".join(author_names_list)
                self.book_details["authors"] = author_names_sentence
        except:
            raise Exception("invalid XML response")


if __name__ == "__main__":

    obj = GoodreadsAPIClient()

    obj.input_url_from_user()

    try:
        obj.get_book_id_from_input_url()
        obj.make_book_api_url()

        try:
            obj.get_book_details()

            # converting the output into json format
            j_book_details = json.dumps(obj.book_details, indent=4)
            print("Output:\n", j_book_details)

        except:
            print("Output:\n", {})

    except:
        print("Output:\nraise an exception InvalidGoodreadsURL")
