import os
import csv

#path to the csvfile

csvpath = os.path.join('Resources', 'budget_data.csv')

#Empty list to add csv values to

months = []
profits = []
change_profit = []
firstrow = True

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile) 
    header = next(csvreader) 

    for row in csvreader:
     
        if firstrow:
            print("firstrow")
            firstrow = False
            last_profit = int(row[1])
        else : 
            change_profit.append(int(row[1]) - profits[-1])
            last_profit = int(row[1])
        months.append(row[0])
        profits.append(int(row[1]))
        

# months totals
total_months =len(months)

#Total Gained Profit
total_profit =sum(profits)

Average_Change =sum(change_profit)/len(change_profit)

Max_profit = max(change_profit)
Decrease_profit = min(change_profit)







print(total_months)
print(total_profit)
print(profits)
print(change_profit)   
print(Max_profit)
print(Decrease_profit)

txt_path = os.path.join("./" + "Result"+".txt")
output =(f"Financial Analysis - \n"
        f"-----------------------------------------\n"
        f"Total Months: {total_months}\n"
        f"-----------------------------------------\n" 
        f"Total Revenue: {total_profit}\n"
        f"-----------------------------------------\n" 
        f"Average Revenue: {Average_Change}\n"
        f"-----------------------------------------\n" 
        f"Greatest Increase in Revenue: {Max_profit}\n"
        f"-----------------------------------------\n" 
        f"Greatest Decrease in Revenue: {Decrease_profit}\n"
        f"-----------------------------------------\n" )
print(output)        
with open(txt_path, "w") as text_file:
    text_file.write(output)
  
