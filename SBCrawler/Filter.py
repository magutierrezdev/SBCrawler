from .Parser import Parser
import re

class Filter():

    def count_words(self,text):
       words = re.findall(r'\b\w+\b', text) 
       return len(words)

    def get_entry(self,dict_entry, values_list): #Receive an dictionary and insert its values into a list to store it into a list of lists (values_list)
        value_list = []
        value_list.append(dict_entry.get('number'))
        value_list.append(dict_entry.get('title'))
        value_list.append(dict_entry.get('score'))
        if dict_entry.get('comments') == "discuss":
            dict_entry['comments'] = 0
        if dict_entry.get('comments') != "discuss":
            value_list.append(int(dict_entry.get('comments')))
        
        values_list.append(value_list)




    def get_more_five_words_ordered_comments(self, order):                
        obj_parser = Parser()    
        list_parsed_data = obj_parser.set_format_entries()
        filtered_list = []
        for i in list_parsed_data:
            if self.count_words(i.get('title')) > 5: #Filtering by title words len
                self.get_entry(i,filtered_list)

        if order == "max":
            entries = sorted(filtered_list, key=lambda x: -x[3]) #entries ordered from highest to lowest number of comments.
        if order == "min":
            entries = sorted(filtered_list, key=lambda x: x[3]) #entries ordered from lowest to highest number of comments.
        
        return entries        


    def get_less_five_words_ordered_points(self,order):
        obj_parser = Parser()    
        list_parsed_data = obj_parser.set_format_entries()
        filtered_list = []
        for i in list_parsed_data:
            if self.count_words(i.get('title')) <= 5: #Filtering by title words len
                self.get_entry(i,filtered_list)
        if order == "max":
            entries = sorted(filtered_list, key=lambda x: -x[2]) #entries ordered from highest to lowest number of comments.
        if order == "min":
            entries = sorted(filtered_list, key=lambda x: x[2]) #entries ordered from lowest to highest number of comments.
        
        return entries

        