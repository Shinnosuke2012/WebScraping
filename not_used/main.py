import os
import json
import requests, bs4
from typing import Dict
from transformers import pipeline
from Scrape import Scrape_html

# Send a GET request to the webpage
res = requests.get('https://www.nature.com/search?q=sodium+ion+battery+cathode+capacity&journal=')
res.raise_for_status()

#parsed html
soup = bs4.BeautifulSoup(res.text, "html.parser")

#h3 elements
elems = soup.select(".u-container h3")

#import model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

#All data will be stored in one dictionary.
paper_scrape: Dict = {}
for i,elem in enumerate(elems):
    print(f'{i+1}/50 processing')

    # title = elem.find("a",class_="c-card__link u-link-inherit").text
    url = "https://www.nature.com"+elem.select("a")[0].get("href")

    #Call the function
    data = Scrape_html(url=url,summarizer=summarizer)

    paper_scrape["id"+str(i+1)] = data
    
    print(f"{i+1}/50 Done.")

#assign path for exporting the result
path = "Output"

with open(os.path.join(path,"output.json"), "w",encoding="utf8") as file:
   json.dump(paper_scrape,file, indent=4)

# print(json.dumps(paper_scrape,indent=4))