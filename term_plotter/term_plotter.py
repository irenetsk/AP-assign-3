from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords 
import os, json, argparse, sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# HANDLING THE ARGUMENTS AND CREATING TITLES
parser.add_argument('--terms', type=str, nargs='+')
parser.add_argument("--path", required=False, default="./us_presidential_speeches")
parser.add_argument('--title', type = str, default="")
parser.add_argument('--output', type =str, required=False, default=None)
args = parser.parse_args()
terms_list, terms_normal = [],[]
for term in args.terms:
    terms_normal.append(term.lower())
    term = term.replace(' ', '_')
    terms_list.append(term.lower())
filename = "_".join(terms_list)
if args.output == None:
    args.output = f"{filename}.png"

def main():
    # 1. TAKING CARE OF STOPWORDS AND NUMBER OF ARGUMENTS
    if len(terms_normal) > 5:
            print("Hey! You have used more than 5 terms, which is not allowed.")
            sys.exit()
    else:
        counter = 0
        stop_words = list(stopwords.words('english'))
        for term in terms_normal:
            if term in stop_words:
                print("Error: You have used a stop-word in the terms, which is not allowed. Try another word.")
                sys.exit()

    #2.1 HANDLING THE SPEECHES
    path = args.path
    try:
        speeches_jsons = [json for json in os.listdir(path) if json.endswith('.json')]
    except:
        print("Path not found.")
        sys.exit()
    speeches_df = pd.DataFrame(columns=['Date', 'Score', 'Term'])
    corpus, combined_jsons = [], []
    for text in speeches_jsons:
        with open(os.path.join(speeches_path, text)) as element:
            json_text = json.load(element)
            combined_jsons.append(json_text)
            corpus.append(json_text["Speech"].lower())

    #2.2 CREATING VECTORS
    vectorizer = TfidfVectorizer(ngram_range=(1,3), stop_words="english")
    vectors = vectorizer.fit_transform(corpus)
    vocab = vectorizer.vocabulary_       

    #2.3 CREATING DATAFRAMES
    for term in terms_normal:
        df_term = pd.DataFrame(columns=['Date', 'Score', 'Term'])
        for index, speech_item in enumerate(combined_jsons):      
            date = pd.to_datetime(speech_item['Date'], yearfirst=True)
            speech = speech_item['Speech'].lower()
            if term in speech:
                column = vocab[term]
                score = vectors[index, column]
            else:
                score = float(0)
            df_term.loc[index] = [date, score, term]
        speeches_df = speeches_df.append(df_term)

    # 3. MAKING CHARTS
    sns.set_theme()
    plot = sns.relplot(data=speeches_df, x="Date", y="Score", kind="line", hue="Term", legend="auto")
    plt.title(args.title)
    plot.savefig(args.output)
    plt.show()   

main()