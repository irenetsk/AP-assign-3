Description

The program is used to visualise term usage in US presidential speeches. 

Instruction

Calling program: python term_plotter.py 
Required arguments: --terms (user provides up to five terms to search for in the speeches. The terms have to be provided in quotation marks)
Optional arguments: --path (path to the folder, where the .json files of speeches can be found. Default argument: "./us_presidential_speeches" folder", which should be found in the same location as the python script term_plotter.py)
--title (title for the diagram created by the program. Given none, there will be no title.)
--output (the filename for the diagram, saved in .png format. Default output: given terms separated by dashes.)

Development

The program uses 10 modules, namely argparse, os, sys, json, nltk, sklearn, pandas, numpy, matplotlib as well as seaborn. 

First, the program handles the arguments using argparse (the description of argparse usage can be found in the README.txt for twitter_query.py), in order to obtain two different versions of terms: 1) terms_normal list where tokens are joined with whitespace and 2) term_dashes where tokens are joined with an underscore. Then function check_terms_stopwords() is called. This function first sets a counter to zero. If the length of the terms in terms_normal is more than five, it prints out a message for the user that only up to five terms are allowed. If the length of the list is acceptable, the program checks for stopwords. In order to do this, stop_words list is created by calling stop words.words() with parameter 'english' from nltk module (stop words have to to be downloaded). Then the function iterates through the term_normal list and checks whether each term is in stop_words. If it is, the program yields a message that stop words cannot be used and stops, and if not it continues.

The next part of the function could be divided into three subparts: handling the speeches, creating vectors and creating dataframes. First, the function uses the os module and iterates through files in the folder specified in args.path. The speeches are saved in .json files as dictionaries, with Date, Speech and Name (of the president) as keys. The function concatenates the contents of speech file and saves it in the speeches_json variable if the file ends with .json by using join(), loading the json file and appending json_text to combined_jsons. It also appends a lowered "speech" value from json_text to corpus. So the end result is two lists: one is combined_jsons, where one can find all the contents of the files found in --path, and the other one is the corpus list, which contains only the combined speeches. 

Then the Vectorizer object from the sklearn module is called and is given parameters to work with unigrams, bigrams and trigrams. The function applies the fit_transform() method of the Vectorizer on corpus, in order to obtain the vector scores of all the terms in the corpus, which come in the form of an array by default, and it is stored in the variable vectors. Then, a variable named vocabulary is created, which is essentially a dictionary that stores pairs of terms and feature indices as key and value.

The third part is concerned with the dataframe's creation. The function iterates through terms_normal and for every term it creates a data frame, with Date, Score and Term columns. It then iterates through enumerated combined_jsons list and assigns date, score and term to the data frame. If the term exists in the speech, a score is obtained from the created array by using the coordinates for row and column (in code: "index" and "column"). If not found, the term is given a float value of zero. This is done for all the terms and then they are concatenated to one general data frame speeches_df.

Finally, the function uses the seaborn module to plot the data from speeches_df. It calls a method relplot(), with the parameters data, x, y, kind, hue, legend predefined for the user. The x axis depicts time, thus it uses the column "Date", y axis depict the frequency of term found in the speech, thus, it uses column "Score". There are different hues used for the terms, they are illustrated in lines. In order to save the figure as .png savefig() method is called, and finally, with the method show(), the plotted data appears in a line chart.