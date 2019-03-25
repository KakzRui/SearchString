### Search String
Search string using google search api and returns top 5 results.

*Steps:*
1. Enter the string to search.
1. Returns the results in json format, can see the data in json file.

*Flow:*
1. main.py is to get the string input from user to search.
1. Calling search_string method.
1. search_string.py calls the google api and returns the result in json format.
1. Results are saved in json file under tmp folder

*TODO:*
1. Better place to save the data.
1. Good to have template to search and view the results.