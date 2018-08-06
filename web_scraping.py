import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('http://mhrd.gov.in/iits')
soup = BeautifulSoup(page.text, 'html.parser')

college_name_list = soup.find(class_ = "dataTable")
college_name_list_items = college_name_list.find_all('td')
college_detail = []
for college in college_name_list_items:
    college_detail.extend(college.contents)

temp = [i for i in college_detail if i!='\n']
final_college_names = []
for i in temp:
    try:
        final_college_names.extend(i.contents)
    except:
        final_college_names.append(i.strip('\n').strip('\t'))

f = csv.writer(open('IITs in India.csv','w'),delimiter=',')
for c in range(0, len(final_college_names),3):
    f.writerows([final_college_names[c:c+3]])