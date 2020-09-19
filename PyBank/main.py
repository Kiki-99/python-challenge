import os
import csv

recordspath = 'Resources/budget_data.csv'
print('Financial Analysis')
print('-----------------------------------------')

with open(recordspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    months = len(list(csvreader))
    print(f'Total Months: {months}')

    



