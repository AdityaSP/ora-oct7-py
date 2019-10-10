# each movies posters in a folder of its own
# multi-threaded application where the downloads can happen in parallel

import requests
import json
ui= input("Movie search string: ")
url = r'http://www.omdbapi.com/?s='+ ui + r'&apikey=b4e17ea0'
r = requests.get(url)
if r.ok:
    data = json.loads(r.text)
    for movie in data['Search']:
        print("Downloading for", movie['Title'])
        if movie['Poster'] != 'N/A':
            poster = requests.get(movie['Poster'])
            if poster.ok:
                fh = open(movie['imdbID'] + '.jpg', 'wb')
                fh.write(poster.content)
                fh.close()