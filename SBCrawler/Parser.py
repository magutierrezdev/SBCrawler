import csv

class Parser():


    def load_file(self,namefile):
        list_entries = []
        with open(namefile, mode ='r')as file:
            csv_file = csv.reader(file, delimiter=";")
            for lines in csv_file:
                list_entries.append(lines)

            list_entries.pop(0) #Removing duplicated
            return list_entries

    def set_format_entries(self):
        
        list_data = self.load_file('results.txt')

        dict_entry = {
            "number": 0,
            "title" : " ",
            "score" : 0,
            "comments": 0 
        }

        dictionary_list = []

        counter = 0
        for i in range(0,len(list_data)): 
            """Storing the information into a list of dictionaries. The access to each key element into the dictionary has a cost of O(1).
                In the worst case, to look for an element into the list has a cost of O(n)
            """
            counter += 1
            dict_entry["number"] = counter
            dict_entry["title"] = list_data[i][0]

            list_data[i][1] = ' '.join(list_data[i][1].split()) #Cleaning the string
            dict_entry["score"] = int(list_data[i][1].split(' ')[0])
            list_data[i][2] = ' '.join(list_data[i][2].split())
            if "comments" in list_data[i][2] or "comment" in list_data[i][2]: #comments can get a integer value and a string value ("discuss").
                dict_entry["comments"] = int(list_data[i][2].split(' ')[0])
            else:
                dict_entry["comments"] = list_data[i][2]

            dictionary_list.append(dict_entry.copy())
        return dictionary_list

