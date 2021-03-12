Description

This program is used for retrieving the most recent tweet as created by a specified user. To do this, it uses tweepy API.

Instruction

Calling program: python twitter_query.py
Required argument: username (the username of the twitter user)
Optional argument: --number (if specified, outputs the amount of tweets specified; if not, the most recent tweet)

Mechanics

The program uses two modules: Tweepy (twitter API) as well as Argparse. 

Tweepy is used to obtain access to twitter's database. One has to obtain consumer key and secret pair as well as access key and secret part in order to authenticate. 


Argparse is used to parse the arguments provided by the user in the terminal. In line 14 we create a variable called parser, which is an ArgumentParser object. After, the program calls the method add_argument() for the required and optional arguments to be stored in the object. Then, the parse_args() method is called and the data stored in the object is transformed into what the developer has specified, in this case, number is of type integer and the default value is 1. 

The program then proceeds to call the function get_tweet().
First the function creates a variable for accessing twitter, which is an API() object from the Tweepy module. Then it tries to use the created object with method user_timeline() in order to obtain the desired result, with the parameters screen_name and count given as those provided by the user fo the program, namely, args.username and args.number. However, if the program encounters an error, TweepError is called and the output of the program is a simple line "Something went wrong :(". Otherwise it will enter a for loop. Which prints the date of the creation of the tweet as well as its contents. In all cases, whether an error is encountered or not, the program outputs ">>> Code executed." in a new line. 


