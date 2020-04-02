import requests
from bs4 import BeautifulSoup

# Some codes for Agah Bashgah leaning bourse videos
# Main web address

url = "https://bashgah.com/blog/دانلود-رایگان-فیلم-آموزش-بورس/"

Bashgah = requests.get(url)  # create HTTP response object

# send a HTTP request to the server and save
# the HTTP response in a response object called Bashgah

# Parse the html webpage
Bashgah_soup = BeautifulSoup(Bashgah.content, "html.parser")

Bashgah_soup_class = Bashgah_soup.find_all(
    'div', attrs={'class': 'wpb_text_column'})

# creating txt for storage collected data

f = open("draft.txt", "w", encoding="utf-8")

for headlines in Bashgah_soup_class:
    subheadlines = headlines.find_all('div', attrs={'class': 'wpb_wrapper'})
    for subhead in subheadlines:
        if len(subhead.text) != 1:
            f.write(subhead.p.text.strip())
f.close()
