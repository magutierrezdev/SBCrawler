# SBCrawler
Stackbuilders Exercise


This Crawler has been developed in Python. To execute it:    
* It is recommended to create a virtual environment. Type in a terminal: python -m venv ./folder_name
* Activate the new venv: source  folder_name/bin/activate
* Install the dependencies using requirements.txt file. Type in the terminal: pip install -r requirements.txt
* Now execute: python3 main.py


The program has a little menu that ask you about that filter or filters do you wish to execute.

* Option 1: filter entries with more than five words in the title ordered by the number of comments first.
* Option 2: filter by entries with less than or equal to five words in the title ordered by points.
* Option 3: execute both filters.

Whichever you choose, you will be asked of what order do you prefer:
* Write max, if you want to order by highest to lowest number of comments or points.
* Write min, if you want to order by lowest to highest number of comments or points.

Then you will see the results.

(There is a crawler.log file with some executions to show some register store from our program)

