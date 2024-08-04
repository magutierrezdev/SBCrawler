from bs4 import BeautifulSoup
import requests

class Crawler:
    

    def get_entries(self, website: str):
        
        headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
        if not website:
            url='https://news.ycombinator.com/'
        else:
            url=website

        response=requests.get(url,headers=headers)


        soup=BeautifulSoup(response.content,'lxml')

        f = open("results.txt", 'w')
        for entry in soup.find_all('tr'):
            try:
                #print(item)
                if entry.select('.titleline > a'):
                    print(entry.select('.titleline > a')[0].get_text(), file=f)

                if entry.select('.hnuser'):
                    print(entry.select('.score')[0].get_text(), file=f)
                    print(entry.find_all('a')[3].get_text(), file=f)

            except Exception as e:
                raise e
                print('')         
        f.close()