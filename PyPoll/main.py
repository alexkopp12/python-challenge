import os
import csv

# Pull in CSV Data
election_data = os.path.join('.', 'PyPoll','Resources_2', 'election_data.csv')


# Define the function and have it accept the 'state_data' as its sole parameter
def write_poll(election_data):

    #Set variables
    votes = 0
    candidates = []
    candidate_1 = ''
    candidate_2 = ''
    candidate_3 = ''
    candidate_1_votes = 0
    candidate_2_votes = 0
    candidate_3_votes = 0
    won = ""

    with open(election_data) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
        csv_header = next(csv_file)
        print(f"Header: {csv_header}")

    # Read through each row of data after the header
        for row in csv_reader:
            #Month Counter
            votes = votes + 1

            if len(candidates) == 0:    
                    candidate_1 = row[2]
                    candidates.append(candidate_1)
            if len(candidates) == 1:    
                if candidate_1 != row[2]:
                    candidate_2 = row[2]
                    candidates.append(candidate_2)
            if len(candidates) == 2:    
                if candidate_2 != row[2]:
                    candidate_3 = row[2]
                    candidates.append(candidate_3)
            
            if row[2] == candidate_1:
                candidate_1_votes = candidate_1_votes + 1
            elif row[2] == candidate_2: 
                candidate_2_votes = candidate_2_votes + 1
            elif row[2] == candidate_3:
                candidate_3_votes = candidate_3_votes + 1
    
    if candidate_1_votes > candidate_2_votes and candidate_1_votes > candidate_3_votes:
        won = candidate_1
    elif candidate_2_votes > candidate_3_votes:
        won = candidate_2
    else:
        won = candidate_3
    



    # Print analysis
    print("Election Results\n")
    print("----------------------------\n")
    print(f"Total Votes: {votes}\n")
    print("----------------------------\n")
    print(f"{candidates[0]}: {round(candidate_1_votes/votes, 2)*100}% ({candidate_1})\n")
    print(f"{candidates[1]}: {round(candidate_2_votes/votes, 2)*100}% ({candidate_2}\n")
    print(f"{candidates[2]}: {round(candidate_3_votes/votes, 2)*100}% ({candidate_3})\n")
    print("----------------------------\n")
    print(f"Winner: {won}\n")

    # Write Analysis
    input_path = './PyPoll/Analysis/Analysis.txt'
    with open(input_path, 'w') as analysis_txt:
        analysis_txt.write("Election Results\n")
        analysis_txt.write("----------------------------\n")
        analysis_txt.write(f"Total Votes: {votes}\n")
        analysis_txt.write("----------------------------\n")
        analysis_txt.write(f"{candidates[0]}: {round(candidate_1_votes/votes, 2)*100}% ({candidate_1})\n")
        analysis_txt.write(f"{candidates[1]}: {round(candidate_2_votes/votes, 2)*100}% ({candidate_2}\n")
        analysis_txt.write(f"{candidates[2]}: {round(candidate_3_votes/votes, 2)*100}% ({candidate_3})\n")
        analysis_txt.write("----------------------------\n")
        analysis_txt.write(f"Winner: {won}\n")

        analysis_txt.close()
    
write_poll(election_data)