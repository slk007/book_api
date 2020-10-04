# book api

**get details of specific books using GOODREADS API link**

* Inside:
  * API
  * requests
  * [test scripts](https://github.com/slk007/book_api/raw/master/test%20scripts.xlsx)
  * xml response

**Requirements**
```
pip install requests
```

# How to use:

**make a config.py file within book_api folder**
**add below link in config.py**
```
developer_key = "<keep your GOODREAD developer key here>"
```


**To run the main file:**
```
python main.py
```
Enter your url when it asks for input

![book_api_snap](https://github.com/slk007/book_api/blob/master/book_api_snap.png)


**To run the test file:**
```
python test_p.py
python test_n.py
```
