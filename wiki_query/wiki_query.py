import requests
from bs4 import BeautifulSoup
import argparse
from urllib.error import HTTPError
import urllib.request
from urllib.parse import quote

parser = argparse.ArgumentParser()
parser.add_argument("page")
args = parser.parse_args()

def get_wiki():
        page = urllib.parse.quote(args.page)
        site_string = f"https://en.wikipedia.org/wiki/{page}"
        try:
            cl_site = urllib.request.urlopen(site_string)
            soup = BeautifulSoup(cl_site, "html.parser")
        except HTTPError:
            print("Wiki page not found.")
        else:
            for par in soup.find_all('p'):
                print(par.get_text())

get_wiki()
