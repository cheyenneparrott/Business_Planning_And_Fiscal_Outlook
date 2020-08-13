# import dependencies
import csv
import os


#declare variable
total_months = []
total_profit_loss = []
profit_loss_change = []

# Load CSV
budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv) as txt_data:
    csvreader = csv.reader(txt_data)
    next(csvreader)

    for row in csvreader:
        total_months.append(str(row[0]))
        total_profit_loss.append(int(row[1]))
    TotalMonths = len(total_months)
    TotalProfitLoss = sum(total_profit_loss)
    for i in range(1,len(total_profit_loss)):
        profit_loss_change.append(int(total_profit_loss[i])-int(total_profit_loss[i-1]))
    average_change = sum(profit_loss_change) / len(profit_loss_change)
    greatest_increase = max(profit_loss_change)
    greatest_decrease = min(profit_loss_change)
    greatest_increase_date = total_months[profit_loss_change.index(greatest_increase)+1]
    greatest_decrease_date = total_months[profit_loss_change.index(greatest_decrease)+1]


# Print the analysis to the terminal
print(f"Financial Analysis")
print(f"-------------------------")
print(f"Total Months: {TotalMonths}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")



# Export a text file with the results
#file_to_output = os.path.join("analysis", "analysis.txt")


