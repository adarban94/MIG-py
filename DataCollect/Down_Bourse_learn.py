import requests
# import re
from bs4 import BeautifulSoup

# Some codes for Agah Bashgah leaning bourse videos

url = "https://bashgah.com/blog/دانلود-رایگان-فیلم-آموزش-بورس/"     # Main web address

Bashgah = requests.get(url)  # create HTTP response object

# send a HTTP request to the server and save
# the HTTP response in a response object called Bashgah

# Parse the html webpage
Bashgah_soup = BeautifulSoup(Bashgah.text, "html.parser")

Bashgah_soup_class = Bashgah_soup.find_all(
    'div', attrs={'class': 'wpb_wrapper'})

for items in Bashgah_soup_class:
    titles = items.p.text.strip()
    subtitles = titles.find_all('a').text.strip()
    print(titles + "\n --------- \n \n")
    for sub in subtitles:
        print(sub + ': ' + sub['href'] + '\n')
