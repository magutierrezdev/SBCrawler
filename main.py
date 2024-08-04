from SBCrawler.Crawler import Crawler
from SBCrawler.Parser import Parser

def main():    

    link = "https://news.ycombinator.com/"
    obj_crawler = Crawler()
    obj_crawler.get_entries(website=link)  #Get data from HackerNews and store them  
    
    obj_parser = Parser()    
    obj_parser.format_entries()


    
if __name__ == '__main__':
    main()