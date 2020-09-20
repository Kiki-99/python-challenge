import os
import csv

recordspath = 'Resources/budget_data.csv'
print('Financial Analysis')
print('------------------------------------------------')


with open(recordspath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header= next(csvreader)

    row_count = sum(1 for row in csvreader)
    csvfile.seek(0)
    next(csvreader)
    
    print(f"Total Months : {row_count}" )

    sum_profit = 0
    sum_loss = 0
    totalPL = 0
    profit = 0

    Net = []
    for row in csvreader:
        Net.append(int(row[1]))

    print(f'Total: {sum(Net)}')

    Average = []
    for row in csvreader:
        Average.append(int(row[1]))
    
    print(f'Average Change: {totalPL/row_count}')





