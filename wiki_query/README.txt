Description

This program is used for obtaining the main text from wikipedia page articles. 

Instruction

Calling the program: python wiki_querry.py
Required arguments: page (the search term as one would provide in the search bar on wikipedia page)

Development

The program uses three modules: bs4, argparse and urlib. The description of argparse use can be found in the README file for twitter_query. The urllib module is used only for requesting the contents of the HTML file. The bs4 module is used to parse the text as provided in HTML format. By creating a BeautifulSoup object, the program converts the provided HTML format file into a more user friendly and readable format. 

First, the program is provided with the arguments, which are parsed by argparse and stored in variable args. Then the program calls get_wiki() function. The function first stores a site_string variable, which uses an f-string to fill in the term specified by the user. The term, however, has been converted by the quote() method in order to allow non-ascii characters. The function tries to obtain the HTML page contents and parse them with BeautifulSoup(). If it succeeds, it will print all the paragraphs found by the find_all() method. Otherwise, if it encounters and HTTPError, it will print "Wiki page not found". 


