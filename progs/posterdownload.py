# each movies posters in a folder of its own
# multi-threaded application where the downloads can happen in parallel

import requests
import json
from threading import Thread
import os

ui= input("Movie search string: ")

if ( os.path.exists(ui)):
    print(ui, "exists.")
    exit(1)
else:
    os.mkdir(ui)

url = r'http://www.omdbapi.com/?s='+ ui + r'&apikey=b4e17ea0'
r = requests.get(url)

def download(posterurl, filename):
    poster = requests.get(posterurl)
    if poster.ok:
        fh = open(filename, 'wb')
        fh.write(poster.content)
        fh.close()    

if r.ok:
    data = json.loads(r.text)
    for movie in data['Search']:
        print("Downloading for", movie['Title'])
        if movie['Poster'] != 'N/A':
            #download(movie['Poster'] , movie['imdbID'] + '.jpg')
            Thread(target=download, args=[movie['Poster'] , ui+os.path.sep+movie['imdbID'] + '.jpg']).start()
            