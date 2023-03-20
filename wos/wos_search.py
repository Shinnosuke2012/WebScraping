"""This module gets url of related pages and exports results as json file.

"""
import os
import json
from typing import Any,Dict
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from wos.scrape import scrape_pages

def extract_info(query:str,count:int,api_key:str,debag:bool=False) -> None:
    """This module gets url of related pages and exports results as json file.

    Args
        query(str):keyword
        count(int):the number of results to return
        api_key(str):your api key

    """
    #keyword
    query = query.replace(" ","+")
    #the index of the first result to return
    start = 1

    #define columns of dataframe
    # columns = ["Title","URL","Author","Publication date","Summary of abstract","Value","Keyword"]
    #create dataframe
    # df = pd.DataFrame(columns=columns)
    #import model

    summarizer : Any = pipeline("summarization", model="facebook/bart-large-cnn")

    # Set up the API request
    import_path:str = f'''
    https://api.clarivate.com/api/wos/?databaseId=WOS&usrQuery={query}&count={count}&firstRecord={start}
    '''

    headers = {
        "X-ApiKey": api_key
    }

    # Make the API request
    response = requests.get(import_path, headers=headers,timeout=None)

    # Process the API response
    if response.status_code == 200:
        # Parse the response HTML with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the unique identifier in the search results URL
        search_results_url = soup.select(".title title-link font-size-18 ng-star-inserted a")
        scraping_results : Dict = {}

        for i,result in enumerate(search_results_url):
            print(f"{i+1}/{count} processing.")
            #url
            page_url = "webofscience.com"+result.select("a")[0].get("href")
            scraping_result = scrape_pages(url=page_url,summarizer=summarizer)
            scraping_results[f"id{i+1}"] = scraping_result
            print(f"{i+1}/{count} done.")

        #assign path for exporting the result
        export_path:str = "Output"

        with open(os.path.join(export_path,"output.json"), "w",encoding="utf8") as file:
            json.dump(scraping_results,file, indent=4)

        if debag is True:
            print(json.dumps(scraping_results,indent=4))

    else:
        print(f"Error: {response.status_code}")
