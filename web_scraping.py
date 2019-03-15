#Web scraping with python and beautifulsoup4 

import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('http://mhrd.gov.in/iits')
soup = BeautifulSoup(page.text, 'html.parser')

college_name_list = soup.find(class_ = "dataTable")

college_name_list_items = college_name_list.find_all('td')

f = csv.writer(open('IITs in India.csv','w'))
f.writerow(['Serial no.       ', 'Name'])

# Remove bottom links
#last_links = soup.find(class_='dataTable')
#last_links.decompose() 
i=0
for college_name in college_name_list_items:
    #print(college_name.prettify())
    names = college_name.contents[0]
    print(names)
    i=i+1
    f.writerow([i,names])updated 
