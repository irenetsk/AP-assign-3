Description

This program is used for creating a text classification model that is able to tag words with their according Part-of-Speech tags.

Instructions

Calling the program in the upper “tagger” folder: 

1. For training:		python3 run.py --mode train --config config.yaml
2. For tagging:		python3 run.py --mode tag --text my_file.txt --config config.yaml
3. For evaluating:	python3 run.py --mode eval --gold my_gold_file.txt --config config.yaml

Required arguments: --mode, --tag (only if mode =.tag), --config
Optional argument: --gold


Mechanics

The program uses the following modules: argparse, pickle, lumpy, yaml, spacy, and sklearn.

The main function “run” is the one from which all the different modes can be called, and it  also imports function from the other files, “model.py”, “config.yaml” and “pre_process.py”. 
For the feature-engineering-concerned function “token_to_features”, which is called from the “prepare_data_for_training” function used for the pre-processing of the data, we decided to add a few extra features:
1. Check to see if the token is punctuation
2. Include the last letter of the token, other than the last 2 and 3 (which were already existing)
3. Check to see if the token has a prefix of 1 or 2 letters
4. Check to see if the token has a suffix of 1 or 2 letters
5. The token that is 2 positions before the investigated token
6. The token that is 2 positions after the investigated token

The model used initially, namely the Linear Support Vector Classification, yielded an accuracy of 93% and an accuracy of 94% with the newly added features. Upon changing the model to the Logistic Regression model (which is used for classification as well), the accuracy decreased to 93% again, which is admittedly not a significant difference. Additionally, the Multinomial Naive Bayes model resulted in an accuracy of 87%.
