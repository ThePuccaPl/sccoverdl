import sys
import requests
from bs4 import BeautifulSoup

try:
    htmldata = requests.get(sys.argv[1]).text

    soup = BeautifulSoup(htmldata, 'html.parser')

    res = soup.find_all('img')

    img_data = requests.get(res[0]['src']).content

    with open('cover.jpg', 'wb') as handler:
        handler.write(img_data)

    print("Download complete, file saved as cover.jpg")

except IndexError:
    print("Please provide a valid link")

except requests.exceptions.MissingSchema:
    print("Please provide a valid link")
