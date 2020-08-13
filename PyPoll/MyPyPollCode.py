# import dependencies
import csv
import os

# Load CSV
election_csv = os.path.join("Resources", "election_data.csv")

#declare variables
total_votes = 0
KhanVotes = 0
CorreyVotes = 0
LiVotes = 0
OTooleyVotes = 0

with open(election_csv) as txt_data:
    csvreader = csv.reader(txt_data)
    next(csvreader)

for column in csvreader:
    total_votes = total_votes + 1
    if column[2] == "Khan":
        KhanVotes = KhanVotes + 1
    elif column[2] == "Correy":
        CorreyVotes = CorreyVotes + 1
    elif column[2] == "Li":
        LiVotes = LiVotes + 1
    else:
        OTooleyVotes = OTooleyVotes + 1
print(LiVotes)



# Define the function and have it accept the 'election_data' as its sole parameter
# def print_votes(election_data):
#     # Assign values to variables with descriptive names
#     voter_id = str(election_data[0])
#     county = str(election_data[1])
#     candidate = str(election_data[2])

# #The total number of votes cast
# total_votes = len(voter_id)

# #A complete list of candidates who received votes
# Need a for loop?

# #The percentage of votes each candidate won
# Need a percentage function

# #The total number of votes each candidate won
# Need a function and for loop that defines the total votes for each candidate

# #The winner of the election based on popular vote.
# Need a function and for loop that defines the max


# # Print the analysis to the terminal
#     print(f"Election Results")
#     print(f"-------------------------")
#     print(f"Total Votes: {int(total_votes)}")
#     print(f"-------------------------")
#     print(f"Khan: ${int(average_change)}")
#     print(f"Correy: )
#     print(f"Li" )
#     print(f"O'Tooley")
#     print(f"-------------------------")
#     print(f"Winner: ")
#     print(f"-------------------------")


txt_data.close