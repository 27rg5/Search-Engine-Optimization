from general import *
from scrape import *
from parsing import *
from demo import *

class crawler:
    project_name=""
    base_url=""
    domain_name=""
    queue_file_name=""
    crawler_file_name=""
    queue=set()
    crawled=set()
    def __init__(self, project_name, base_url, domain_name):
        crawler.project_name=project_name
        crawler.base_url=base_url
        crawler.domain_name=domain_name
        crawler.queue_file_name=crawler.project_name + '/queue.text'
        crawler.crawler_file_name=crawler.project_name + '/crawled.text'
        base(base_url)
        self.boot()
        self.crawl_page("first thread","sourcefile.html")

    @staticmethod
    def boot():
        create_directory(crawler.project_name)
        crete_files(crawler.project_name,"sourcefile.html")
        crawler.queue=file_to_set(crawler.queue_file_name)
        crawler.crawled=file_to_set(crawler.crawler_file_name)
    
    @staticmethod
    def crawl_page(threadName,page_url):
        if page_url not in crawler.crawled:
            print(threadName + ' now crawling ' + page_url)
            print('Queue ' + str(len(crawler.queue)) + ' | Crawled  ' + str(len(crawler.crawled)))
            crawler.add_links_to_queue(crawler.gather_links(page_url))
            crawler.queue.remove(page_url)
            crawler.crawled.add(page_url)
            crawler.update_files()

    @staticmethod
    def gather_links(page_url):
        try:
            finder = parsing(crawler.base_url, page_url)
            finder.find_links(page_url)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()


    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in crawler.queue) or (url in crawler.crawled):
                continue
            if crawler.domain_name != get_domain_name(url):
                continue
            crawler.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(crawler.queue, crawler.queue_file_name)
        set_to_file(crawler.crawled, crawler.crawler_file_name)


    


    