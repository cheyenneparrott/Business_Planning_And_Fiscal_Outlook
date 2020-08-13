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
Winner = max(KhanVotes, CorreyVotes, LiVotes,OTooleyVotes)

percentage_khan = (KhanVotes / total_votes) * 100
percentage_correy = (CorreyVotes / total_votes) * 100
percentage_li = (LiVotes / total_votes) * 100
percentage_otooley = (OTooleyVotes / total_votes) * 100


if Winner == KhanVotes:
    winner = "Khan"
elif Winner == CorreyVotes:
    winner = "Correy"
elif Winner == LiVotes:
    winner = "Li"
else: winner = "O'Tooley"

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"Khan: {round(percentage_khan,3)}% ({KhanVotes})")
print(f"Correy: {round(percentage_correy,3)}% ({CorreyVotes})")
print(f"Li: {round(percentage_li,3)}% ({LiVotes})")
print(f"O'Tooley: {round(percentage_otooley,3)}% ({OTooleyVotes})")
print(f"-------------------------")
print(f"Winner: {winner}")


txt_data.close()