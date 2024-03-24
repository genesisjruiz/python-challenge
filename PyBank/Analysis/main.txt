'''
PyBank Instructions:
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
Your task is to create a Python script that analyzes the records to calculate each of the following values:
The total number of months included in the dataset
The net total amount of "Profit/Losses" over the entire period
The changes in "Profit/Losses" over the entire period, and then the average of those changes
The greatest increase in profits (date and amount) over the entire period
The greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
'''
# Import the modules
import os
import csv

#Set the path to the CSV file 
csvpath = r'C:\Users\gruiz\desktop\bootcamp\repos\python-challenge\Pybank\resources\budget_data.csv'

# Open the CSV 
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile)

    # Skip the header row
    next(csvreader)

   # Set variables
    total_months = 0
    total_profit_loss = 0
    previous_profit_loss = None
    total_change = 0

    # Set variables for greatest increase and decrease in profits
    greatest_increase = 0
    greatest_increase_month = ''
    greatest_decrease = 0
    greatest_decrease_month = ''

    # Loop through each row in the CSV file
    for row in csvreader:
        # Check if the date column is not empty
        if row[0] != '':
            total_months += 1
            profit_loss = int(row[1])

            # Calculate the change in profit/loss since the previous month
            if previous_profit_loss is not None:
                change = profit_loss - previous_profit_loss
                total_change += change

                # Check if the change is the greatest increase or decrease
                if change > greatest_increase:
                    greatest_increase = change
                    greatest_increase_month = row[0]
                elif change < greatest_decrease:
                    greatest_decrease = change
                    greatest_decrease_month = row[0]

            previous_profit_loss = profit_loss
            total_profit_loss += profit_loss

# Calculate the average change
average_change = total_change / (total_months - 1)  # Subtracted 1 for the first month without change data

# Set output path to write to a text file
output_path = r'C:\Users\gruiz\desktop\bootcamp\repos\python-challenge\Pybank\analysis\financial_analysis.txt'

with open(output_path, 'w') as txtfile:
    # Write the analysis to the file
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

# Print the analysis to the console as well
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

print("\nResults have been written to financial_analysis.txt")