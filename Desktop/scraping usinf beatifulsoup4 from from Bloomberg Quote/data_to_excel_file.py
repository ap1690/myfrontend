import csv
from datetime import datetime
# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	writer.writerow([name, price, datetime.now()])
Now if you run your program, you should ab