'''
PyPoll Instructions:
In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote

Your analysis should align with the following results:

Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
-------------------------
Winner: Diana DeGette
-------------------------
In addition, your final script should both print the analysis to the terminal and export a text file with the results.
'''
# Import the modules
import os
import csv

# Set the path to the CSV file
csvpath = r'C:\Users\gruiz\desktop\bootcamp\repos\python-challenge\pypoll\resources\election_data.csv'

# Set variables
total_votes = 0
candidate_votes = {}  # Dictionary to store candidate votes

# Open the CSV
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the header row
    next(csvreader)

    # Iterate through rows to count total votes and candidate votes
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2] #Corresponds to row index 1 and coloumn index 2. (0-based indexing)

        # Candidate_votes dictionary
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Calculate and print the results & header
print("Election Results")
print("----------------------------")
print(f'Total Votes: {total_votes}')
print("----------------------------")

# Iterate through candidate_votes dictionary to print each candidate's results
winner = max(candidate_votes, key=candidate_votes.get)
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    formatted_percentage = f'{percentage:.3f}%'
    print(f'{candidate}: {formatted_percentage} ({votes})')

print("----------------------------")
print(f'Winner: {winner}')
print("----------------------------")