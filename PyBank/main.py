import os
import csv

# Pull in CSV Data
budget_data = os.path.join('.', 'Resources', 'budget_data.csv')


# Define the function and have it accept the 'state_data' as its sole parameter
def write_analysis(budget_data):

#Set variables
    months = 0
    net_profit = 0
    delta = 0
    prev_profit = 0
    net_profit_delta = 0
    inc_max = ['', 0]
    dec_max = ['', 0]


    with open(budget_data) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
        csv_header = next(csv_file)
        print(f"Header: {csv_header}")

    # Read through each row of data after the header
        for row in csv_reader:
            #Month Counter
            months = months + 1

            #Net Profit calc
            net_profit = net_profit + int(row[1])

            #Delta calc
            delta = int(row[1]) - prev_profit
            

            if dec_max[1] > delta:
                dec_max[0] = row[0]
                dec_max[1] = delta
            elif inc_max[1] < delta:
                inc_max[0] = row[0]
                inc_max[1] = delta

            #Net Profit Change
            net_profit_delta = net_profit_delta + delta

            prev_profit = int(row[1])



            

    # Print analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${net_profit}")
    print(f"Average Change: ${net_profit_delta/months}")
    print(f"Greatest Increase in Profits: {inc_max}")
    print(f"Greatest Decrease in Profits: {dec_max}")

    # Write Analysis
    input_path = './Analysis/Analysis.txt'
    with open(input_path, 'w') as analysis_txt:
        analysis_txt.write("Financial Analysis\n")
        analysis_txt.write("----------------------------\n")
        analysis_txt.write(f"Total Months: {months}\n")
        analysis_txt.write(f"Total: ${net_profit}\n")
        analysis_txt.write(f"Average Change: ${net_profit_delta/months}\n")
        analysis_txt.write(f"Greatest Increase in Profits: {inc_max}\n")
        analysis_txt.write(f"Greatest Decrease in Profits: {dec_max}\n")
        analysis_txt.close()

write_analysis(budget_data)

