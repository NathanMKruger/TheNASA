from bs4 import BeautifulSoup
import requests

def main():
  site = input("Enter URL: ")
  
if __name__ == "__main__":
  main()

def getSiteTitle(site):
  header = requests.utils.default_headers()
  req = requests.get(site, header)
  
  soup = BeautifulSoup(req.content, 'html.parser')
   
  soup.prettify()

  siteTitle = ''
  
  if site.find("title") is not None:
    siteTitle = site.find("title")
  elif site.find("h1") is not None:
    siteTitle = site.find("h1")
 
 return siteTitle
