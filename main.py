from SBCrawler.Crawler import Crawler

def main():    

    link = "https://news.ycombinator.com/"
    obj_crawler = Crawler()
    obj_crawler.get_entries(website=link)  #Get data from HackerNews and store them  

    
    list_entries = []

    with open("results.txt") as archivo:
        for linea in archivo:
            list_entries.append(linea)
    



    
if __name__ == '__main__':
    main()