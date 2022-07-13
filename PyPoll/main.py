#import csv file
import os
import csv

#pathway to file location
csvpath = os.path.join(".", "Resources", "election_data.csv")

#Create variables for vote tallies
TotalVotes = 0
S_votes = 0
DG_votes = 0
D_votes = 0


#open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csvheader = next(csvreader)

    #loop through the rows wtihin csv file
    for row in csvreader:

        #add one vote for every ballot cast
        TotalVotes +=1

        #conditional that adds one to candidate's total when their name is detected in the Candidate column
        if row[2] == "Charles Casper Stockham":
            S_votes +=1
        elif row[2] == "Diana DeGette":
            DG_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            D_votes +=1

#created dictionary containing candidates
Candidates = ["Stockham", "DeGette", "Doane"]
#created dictionary for vote totals
votes = [S_votes, DG_votes, D_votes]

#match up the candidate with their respective vote totals since both dictionaries were listed in order
match = dict(zip(Candidates,votes))

#determine the winner by using max to pull the largest value from the three candidates
winner = max(match, key=match.get)

#calculate the vote percentages
S_percent = (S_votes/TotalVotes)*100
DG_percent = (DG_votes/TotalVotes)*100
D_percent = (D_votes/TotalVotes)*100

#print results
print("Election Results")
print("-----------------------")
print(f"Total Votes: {TotalVotes}")
print("-----------------------")
print(f"Charles Casper Stockham: {S_percent}% ({S_votes})")
print(f"Diana DeGette: {DG_percent}% ({DG_votes})")
print(f"Raymon Anthony Doane: {D_percent}% ({D_votes})")
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")

#export results to text file
exportfile = os.path.join(".", "Resources", "analysis", "Py_Poll_Analysis.txt")
with open(exportfile, "w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("-----------------------")
    file.write("\n")
    file.write(f"Total Votes: {TotalVotes}")
    file.write("\n")
    file.write("-----------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {S_percent}% ({S_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {DG_percent}% ({DG_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {D_percent}% ({D_votes})")
    file.write("\n")
    file.write("-----------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("-----------------------")