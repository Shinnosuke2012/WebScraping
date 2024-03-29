import requests
from bs4 import BeautifulSoup
import re
from typing import Any,Dict

def Scrape_html(url:str,summarizer:Any)->None:
  """This module scrapes abstraction and extracts the value of capacity.

  Args
    url(str) : url of paper

  """

  #Journal name can be searched from url
  #class_name(necessary for scraping abstraction)
  
  if len(re.findall(r'acs',url))>0:
    publisher = "acs"

  elif len(re.findall(r'sciencedirect',url))>0:
    publisher = "sciencedirect"

  elif len(re.findall(r'iopscience',url))>0:
    publisher = "iopscience"

  elif len(re.findall(r'wiley',url))>0:
    publisher = "Wiley"
    class_name = "article-section__content en main"

  elif len(re.findall(r'rsc',url))>0:
    publisher = "Royal Society of Chemistry"

  elif len(re.findall(r'mdpi',url))>0:
    publisher = "MDPI"

  elif len(re.findall(r'springer',url))>0:
    publisher = "Springer"

  elif len(re.findall(r'nature',url))>0:
    publisher = "Nature"
    class_name = "c-article-section__content"

  else:
    publisher = "Others"

  #open web page
  response = requests.get(url)

  # Parse the HTML content using BeautifulSoup
  soup = BeautifulSoup(response.content, 'html.parser')

  #title
  title = soup.find('title').text.replace('−1','-1').replace(' ','')

  #publication date
  date = soup.find("ul",class_="c-article-identifiers").find("a").text

  #author
  author = soup.find("li",class_="c-article-author-list__item").text + " et al."

  # Find the HTML element that contains the abstract
  abstract = soup.find('div',class_=class_name).text.replace('−1','-1').replace(' ','')

  #summarize abstract with 50~100 words
  summary = summarizer(abstract, max_length=100, min_length=50, do_sample=False)[0]["summary_text"]

  #search the value of capacitance from abstract
  pattern = r'[0-9]+\.*[0-9]*\s*m\s*A\s*h\s*g-1'
  capacity = {}
  
  for i,m in enumerate(re.findall(pattern, abstract)):
    capacity["value"+str(i+1)] = m.replace(' ','')

  data: Dict = {"title":title,"publication_date":date,"author":author,"url":url, "publisher":publisher,"summary of abstract":summary,"capacity":capacity}
  
  return data