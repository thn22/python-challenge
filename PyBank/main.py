#import csv file
import os
import csv

#pathway to file location
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#Make lists for code to iterate through desired rows
Months=[]
Profits=[]
MonthlyChange=[]

#open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    #allign months with first column and profits with second column
    for row in csvreader:
        Months.append(row[0])
        Profits.append(int(row[1]))

    #Create variables to hold total months and total profits calculations
    TotalMonths= len(Months)
    TotalProfit= sum(Profits)

    #use loop to run through each row (-1 to offset starting at 0)
    for i in range(len(Profits)-1):

        #subtracts next month from previous to find profit change
        MonthlyChange.append(Profits[i+1]-Profits[i])
    
    #Create variable to hold average change calculation
    AverageChange= (sum(MonthlyChange))/(len(MonthlyChange))


#use min and max to select most and least profitable months
GreatestIncrease = max(MonthlyChange)
GreatestDecrease = min(MonthlyChange)

#Create variable to hold greatest monthly increase and decrease
GI_month = MonthlyChange.index(max(MonthlyChange))+ 1
GD_month = MonthlyChange.index(min(MonthlyChange))+ 1

#print results
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Total: ${TotalProfit}")
print(f"Average Change: {AverageChange}")
print(f"Greatest Increase in Profits: {Months[GI_month]} ${str(GreatestIncrease)}")
print(f"Greatest Decrease in Profits: {Months[GD_month]} ${str(GreatestDecrease)}")

#Printing and exporting results to text file
exportfile = os.path.join("..", "Resources", "analysis", "Py_Bank_Analysis.txt")
with open(exportfile, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("--------------------------")
    file.write("\n")
    file.write(f"Total Months: {TotalMonths}")
    file.write("\n")
    file.write(f"Total: ${TotalProfit}")
    file.write("\n")
    file.write(f"Average Change: {AverageChange}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {Months[GI_month]} ${str(GreatestIncrease)}")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {Months[GD_month]} ${str(GreatestDecrease)}")