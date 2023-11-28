import csv
import os

#Set path for csv file - absolute path was used for development - has been changed to relative path for GitHub
budget_data = os.path.join("PyBank","Resources","budget_data.csv")

#Initialise variables
total_months = 0
total_amount = 0
changes = []
prev_amount = None

#Initialise variables for greatest increase and decrease in profits/losses
greatest_increase = {"Date": "","Amount":float("-inf")}
greatest_decrease = {"Date": "", "Amount":float("inf")}

#Read the CSV file and store the header
with open ("budget_data.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    #Define variables in each column
    months = []
    profit_losses = []

    #loop through each row of the file to get the month and the profits/loss
    for row in csv_reader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

        #Count the total number of months in the dataset
total_months = len(months)
    
        #Calculate the net total amount of Profit/Loss 
net_total = sum(profit_losses)     

        #Calculate the changes in "Profit/Losses" over the entire period


for i in range(1, total_months):
    change = profit_losses[i] - profit_losses[i-1]
    changes.append(change)

            #Check for greatest increase in profits 
greatest_increase = max(changes)
greatest_increase_date = months[changes.index(greatest_increase) + 1]

            #Check for greatest decrease in profits
greatest_decrease = min(changes)
greatest_decrease_date = months[changes.index(greatest_decrease) + 1]

#Calculate average change in Profit/Loss
average_change = sum(changes) / len(changes)

#Print and save the analysis
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change: .2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#Save the output file path
output_path = os.path.join ("PyBank", "Resources_Analysis", "PyBank.txt")

#Open the file using “write” mode. Specify the variable to hold the contents
#Open and print output in text file
file = open("PyBank.txt", "w")
file.write("Financial Analysis\n")
file.write("-------------------------\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${net_total}\n")
file.write(f"Average Change: ${average_change: .2f}\n")
file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
file.close

