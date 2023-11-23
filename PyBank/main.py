import csv
import os

#Set path for csv file - absolute path was used for development - has been changed to relative path for GitHub

#Initialise variables


#Initialise variables for greatest increase and decrease in profits/losses


#Read the CSV file and store the header
with open (budget_data, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    #Define variables in each column
    
        #Count the total number of months in the dataset
        

        #Calculate the net total amount of Profit/Loss 
        

        #Calculate the changes in "Profit/Losses" over the entire period
        

            #Check for greatest increase in profits 
            

            #Check for greatest decrease in profits
            

        

#Calculate average change in Profit/Loss


#Print and save the analysis


#Save the output file path


#Open and print output in the text file 