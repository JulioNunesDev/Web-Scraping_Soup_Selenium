
from bs4 import BeautifulSoup
import requests


content = requests.get('https://olhardigital.com.br/')

context = content.content

site = BeautifulSoup(context, 'html.parser')

## post-list 

postListsTitle = site.findAll('div', attrs={'class': 'post-title'})
postListsSub = site.findAll('div', attrs={'class': 'post-excerpt'})
links = site.findAll('a', attrs={'class': 'card-post'})


titles = []
subtitles = []
linkshref = []



for postlist in postListsTitle:
    titles.append(postlist.text)
   
for postlistsub in postListsSub:
    subtitles.append(postlistsub.text)

   
for teste in links:
    linkshref.append(teste['href'])



mydict = {}

mydict['titles'] = titles
mydict['subtitles'] = subtitles 
mydict['links'] = linkshref

print(mydict)

