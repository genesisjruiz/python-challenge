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

# set output path to write to a text file
output_path = r'C:\Users\gruiz\desktop\bootcamp\repos\python-challenge\pypoll\analysis\election_results.txt'

with open(output_path, 'w') as txtfile:
    # Write the header & total votes
    txtfile.write("Election Results\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write("----------------------------\n")

    # Print and write the candidate results
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        formatted_percentage = f'{percentage:.3f}%'
        result_line = f'{candidate}: {formatted_percentage} ({votes})\n'
        
        print(result_line, end='')  # Print to terminal
        txtfile.write(result_line)  # Write to file

    # Determine and write the winner
    winner = max(candidate_votes, key=candidate_votes.get)
    winner_line = f'Winner: {winner}\n'

    print("----------------------------")
    print(winner_line, end='')
    print("----------------------------")

    # Write the footer lines to the file
    txtfile.write("----------------------------\n")
    txtfile.write(winner_line)
    txtfile.write("----------------------------\n")

print("Results have been exported to election_results.txt")