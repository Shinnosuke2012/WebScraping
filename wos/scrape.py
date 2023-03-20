"""This module scrapes abstraction essential information from papers.
"""
import re
from typing import Any,List,Dict
import requests
from bs4 import BeautifulSoup

def scrape_pages(url:str,summarizer:Any) -> Dict:
    """This module scrapes abstraction and extracts the value of capacity.

    Args
        url(str) : url of the page
        summarizer(Any) : BERT model which summarizes the abstract of the paper.
    
    Returns
        scraping_result(Dict) : dictionary that contains scraped information.

    """
    #open web page
    response = requests.get(url,timeout=None)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    #title
    title:str = soup.find("h2",class_="title text--large").text.replace(' ','')

    #author
    author:str = soup.find("span",class_="font-size-14 value").text + " et al."

    #Publish date
    date: str = soup.find("span",class_="value").text

    #abstract
    abstract : str = soup.find("div", class_="abstract--instance")

    #keyword
    keyword: List = [k.text for k in soup.find_all("span", class_="value ng-star-inserted")]

    #summarize abstract with 50~100 words
    summary = summarizer(abstract,
                         max_length=100,
                         min_length=50,
                         do_sample=False)[0]["summary_text"]

    #search the value of capacitance from abstract
    pattern = r'[0-9]+\.*[0-9]*\s*m\s*A\s*h\s*g-1'
    #extract values from the abstract
    val_extracted :List = [value.replace(' ','') for value in re.findall(pattern, abstract)]

    scraping_result:Dict = {"Title":title,
                            "URL":url,
                            "Author":author,
                            "Publication date":date,
                            "Summary of Abstract":summary,
                            "Value":val_extracted,
                            "Key Word":keyword}

    return scraping_result
