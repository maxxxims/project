import urllib.request
import re
from urllib.parse import quote

def YouTube_request(text, j = 0):

    html = urllib.request.urlopen("https://www.youtube.com/results?search_query={0}".format(quote(text)))
    data = html.read().decode()
    sources = re.findall(r"watch\?v=(\S{11})", data)
    result = 'https://www.youtube.com/watch?v=' + sources[j%9]
    return result

if __name__ == '__main__':
    print(1)