print("MiniMailClient")

import urllib.request
page = urllib.request.urlopen('https://duckduckgo.com/?t=h_&q=billie+eilish&iax=images&ia=images')
print(page.read())