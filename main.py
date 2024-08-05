from SBCrawler.Crawler import Crawler
from SBCrawler.Parser import Parser
from SBCrawler.Filter import Filter
import logging


def launching_crawler():
    print("Launching crawler\n")
    link = "https://news.ycombinator.com/"
    obj_crawler = Crawler()
    obj_crawler.get_entries(website=link)  #Get data from HackerNews and store them  
    logging.info('Crawler launched')
    print("Done\n")

def get_user_choice():
    print("Please, write 1 if you wish to filter by words more than five words and ordered by comments")
    print("Or write 2 if you wish to filter by words less than five words and ordered by points")
    print("Or write 3 to execute all the filters")
    choice = str(input())
    return choice

def get_user_selection():
    print("Please write max, you want to order by highest to lower or write min if you want to order by lowest to highest\n")
    choice = str(input())
    return choice

def filters_execution():
    obj_filter = Filter()
    choice = get_user_choice()
    if choice == "1" or choice == "2" or choice == "3":            
        order = get_user_selection()
        if order == "min" or order == "max":       
            if choice == "1":        
                print(obj_filter.get_more_five_words_ordered_comments(order))
                logging.info('filter by words more than five words and ordered by comments selected')
            if choice == "2":
                print(obj_filter.get_less_five_words_ordered_points(order))
                logging.info('filter by words less than five words and ordered by points selected')
            if choice == "3":
                print("\nFiltering by words more than five words and ordered by comments")
                print("-------------------------------------------------------------")
                print(obj_filter.get_more_five_words_ordered_comments(order))
                logging.info('filter by words more than five words and ordered by comments selected')
                print("\nFiltering by words less than five words and ordered by points")
                print("-------------------------------------------------------------")
                print(obj_filter.get_less_five_words_ordered_points(order))
                logging.info('filter by words less than five words and ordered by points selected')                
        else:
            logging.error('User has written an incorrect filter order: ' + str(order))    
    else:
        logging.error('User has written an incorrect choices: ' + str(choice))



def main():    
    #Including a log to store timestamp, filters selection and errors
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S',filename="crawler.log")
    launching_crawler()
    
    #Including a little interface by command to execute or Crawler and allow to select filters
    filters_execution()
    


if __name__ == '__main__':
    main()