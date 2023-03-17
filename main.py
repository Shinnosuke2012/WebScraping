import os
import json
from typing import List, Dict
from Scrape import Scrape_html

# Send a GET request to the webpage
urls: List = ["https://www.nature.com/articles/s41467-021-22523-3",
        "https://www.nature.com/articles/s41467-021-25610-7",
        "https://www.nature.com/articles/ncomms14283",
        "https://www.nature.com/articles/s41467-019-09933-0"]

#All data will be stored in one dictionary.
paper_scrape: Dict = {}

for i,url in enumerate(urls):
  #Call the function
  data = Scrape_html(url=url)

  paper_scrape["id"+str(i+1)] = data

#assign path for exporting the result
path = "Output"

with open(os.path.join(path,"output.json"), "w",encoding="utf8") as file:
            json.dump(paper_scrape,file, indent=4)

# print(json.dumps(paper_scrape,indent=4))