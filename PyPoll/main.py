import csv
import os

#set path for csv file
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

#Read the csv file and store the header
with open("election_data.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    #Define variables
    total_votes = 0
    candidates = {}
    results = []

    for row in csv_reader:
        candidate = row[2]
        total_votes += 1
        candidates[candidate] = candidates.get(candidate, 0) + 1

#Percentage of votes each candiate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append((candidate, percentage, votes))  

#Winner based on popular vote
winner = max(results, key=lambda x: x[2])

#Print and save the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, percentage, votes in results:
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner[0]}")
print("-------------------------")

#Save the output file path
output_path = os.path.join ("PyPoll", "Analysis", "PyPoll.txt")

#Open the file using “write” mode. Specify the variable to hold the contents
#Open and print output in text file
file = open("PyPoll.txt", "w")
file.write("Election Results\n")
file.write("-------------------------\n")
file.write(f"Total Votes: {total_votes}\n")
file.write("-------------------------\n")
for candidate, percentage, votes in results:
    candidates = f"{candidate}: {percentage:.3f}% ({votes})\n"
    file.write(candidates)
file.write("-------------------------\n")
file.write(f"Winner: {winner[0]}")
file.close
