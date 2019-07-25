import requests
from bs4 import BeautifulSoup
#import module
import csv
for i in range(2):
        in_put=int(input("Enter the Player ID:"))
        url="http://howstat.com/cricket/Statistics/Players/PlayerProgressBat_ODI.asp?PlayerID="+str(in_put)
        page =  requests.get (url)
        soup = BeautifulSoup(page.content, 'html.parser')

        for_name = soup.select("td .Banner2")
        name = [n.get_text() for n in for_name]
        split_name = "".join(name)
        split_selector = "".join(split_name.split("-"))
        final_name = split_selector.split()
        final_player_name = final_name[0] + " " + final_name[1] + " " + final_name[2]
        print(final_player_name)

        main_div =  soup.find(class_ = "TableLined")

        for_run = main_div.select("td .AsteriskSpace")
        run = [r.get_text() for r in for_run]

        run_string = "".join(run)

        initial_run = run_string.split()

        run_index = []
        for items in range(len(initial_run)):
                if (initial_run[items]!= "-"):
                    run_index.append(initial_run[items])
        final_run4 = run_index
        # for numbers in range(1, len(final_run4) + 1):
                # print(numbers)
        # print(final_run4)
       
        with open('ata.csv', 'w+') as wr:
            writer = csv.writer(wr)
            writer.writerows([c.strip() for c in r.split(',')] for r in final_run4)
        wr.close()











               
