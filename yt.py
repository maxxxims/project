import urllib.request
import re

from urllib import request
from urllib.parse import quote
import webbrowser

def YouTube_request(text):

    html = urllib.request.urlopen("https://www.youtube.com/results?search_query={0}".format(quote(text)))
    data = html.read().decode()
    sources = re.findall(r"watch\?v=(\S{11})", data)
    result = 'https://www.youtube.com/watch?v=' + sources[0]
    return result

if __name__ == '__main__':
    msg = 'включи kizaru money long'
    print(msg[7:])