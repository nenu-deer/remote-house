import requests
from bs4 import BeautifulSoup
import pprint
import json

r = requests.get("https://pubchem.ncbi.nlm.nih.gov/rest/autocomplete/compound/aspirin/jsonp?limit=6")
r.encode = "utf-8"
print(r.text)