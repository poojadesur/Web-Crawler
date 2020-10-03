from urllib.request import urlopen
from link_finder import LinkFinder
from start import *

class Spider:

    # class variables (shared among all instances) dont have to set value yet, any spider can set val that stays the same
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()         #stored in ram bc its a variable, faster than hardware where files are saved

    def __init__(self,project_name,base_url,domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First spider',Spider.base_url)
    
    @staticmethod
    def  boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)
    
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_link(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()
    
    @staticmethod
    def gather_link(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            # print("get header thingy: " + response.getheader('Content-Type') + '\n')
            if response.getheader('Content-Type') == 'text/html; charset=UTF-8':
                html_bytes = response.read()
                html_string = html_bytes.decode("UTF-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
            # print('links are ' + finder.page_links)
        except:
            print('Error: can not crawl page')
            return set()
        return finder.page_links()
    
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domain_name not in url:        #dont want it to go through all google and youtube links
                continue
            Spider.queue.add(url)
    
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)



    
    
