from SBCrawler.Crawler import Crawler
from SBCrawler.Parser import Parser
from SBCrawler.Filter import Filter

def main():    

    link = "https://news.ycombinator.com/"
    obj_crawler = Crawler()
    obj_crawler.get_entries(website=link)  #Get data from HackerNews and store them  
    
    list_parsed_data = [] 
    obj_parser = Parser()    
    list_parsed_data = obj_parser.set_format_entries()
    
    """
    for i in list_parsed_data:
        print(i)
    """    

    obj_filter = Filter()
    
    order = "max"
    
    #print(obj_filter.get_more_five_words_ordered_comments(order))


    #print(obj_filter.get_less_five_words_ordered_points(order))



    
if __name__ == '__main__':
    main()