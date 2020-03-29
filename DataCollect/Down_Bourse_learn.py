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
    'div', attrs={'class': 'wpb_wrapper'})

for items in Bashgah_soup_class:
    if items.ul is not None:
        titles = items.p.text.strip()
        subtitles = items.ul.find_all('li')
        print(titles + "\n --------- \n ")
        for sub in subtitles:
            subpage = sub.a["href"]
            subtext = sub.a.text

            subpage_url = requests.get(subpage)
            subpage_soup = BeautifulSoup(subpage_url.content, "html.parser")
            subpage_soup_class = subpage_soup.find(
                'div', attrs={'class': 'px-30 container content'})
            if subpage_soup_class is not None:
                check_videos = subpage_soup_class.find_all(
                    'a', attrs={'rel': "noopener noreferrer"})
                for videos_ls in check_videos:
                    if videos_ls is not None and ".mp4" in videos_ls["href"]:

                        video_href = videos_ls["href"]
                        print(subtext + ": " + video_href + '\n')
