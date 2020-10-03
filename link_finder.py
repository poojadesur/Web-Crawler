from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse

class LinkFinder(HTMLParser):  #inherit stuff from htmlparser
    
    def __init__(self,base_url, page_url):
        # print('link finder initialised')
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self,tag,attrs):
        # print('printing from handle starttag')
        if tag == 'a':     #only on links
            for (attribute, value) in attrs:        #from html parser itself
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)
        # else:
        #     print('here bitch')
        # print(self.links)
        # print('the first linke is ' + x)
        # print('printing from link finder: ')

    # def handle_starttag(self,tag,attrs):
    #     print(tag)
    
    def page_links(self):
        return self.links


    def error(self,message):        #from htmlparser function
        pass

# response = urlopen('https://web.iiit.ac.in/~pooja.desur/index.html')
# html_bytes = response.read()
# html_string = html_bytes.decode("UTF-8")
# print(html_string)
# finder = LinkFinder('https://web.iiit.ac.in/~pooja.desur/index.html','https://web.iiit.ac.in/~pooja.desur/index.html')       #creating LinkFinder object
# # # put stuff in object -  
# finder.feed(html_string)
