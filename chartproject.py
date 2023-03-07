#!/usr/bin/python3

# Import necessary libraries
import os
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

#############################################Functions##############################################

def CalculateBarWidth(val):
    return int(val / 5000)

def seats(party):
    global tvotes
    svotes = int(tvotes / 120)
    n = int(party / svotes)
    return n

#################################################Main###############################################

# Determine console clear command based on operating system
if os.name == "nt":
    console_clear = "cls"
else:
    console_clear = "clear"

# Clear console
os.system(console_clear)

# Print header information
print("Welcome to the Election Results Analyzer!\n")

# Get filename from user input
filename = input("Please enter the filename (including path if necessary): ")

# Try to open and read the input file
try:
    with open(filename, mode="r") as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader) # skip header row
        votes = {rows[0]: int(rows[1]) for rows in csv_reader}
except FileNotFoundError:
    print("Invalid filename or file destination. Exiting program. \n")
    sys.exit()

# Print message indicating that file has been loaded
print("\nFile loaded. \n")

# Calculate total votes and seat counts
tvotes = sum(votes.values())
pvotes = []
tseats = 0

# Print party-wise vote count and seat allocation
print("{:<30s}{:>9s} %5s".format("Party","Votes") %("Seats"))
for party in sorted(votes):
    nvotes = votes[party]
    bar = "#" * CalculateBarWidth(nvotes)
    s = seats(nvotes)
    tseats += s
    print("{:<30s}{:>9d} %5i %s".format(party,nvotes) %(s,bar))
    pvotes.append(nvotes)

# Print total vote count and seat allocation
print(f"\nThere were {tvotes:,} total votes, and {tseats:,} seats allocated.\n")

# Prepare data for plotting
party_names = sorted(votes.keys())
x = np.array(range(0, len(votes)))

# Plot bar chart of party-wise vote counts
plt.xticks(x, party_names, rotation=90, fontsize=8)
plt.bar(x, pvotes, color="g", align="center")
plt.xlabel("Parties")
plt.ylabel("Number of Votes")
plt.title("Election Results")
plt.gcf().subplots_adjust(bottom=0.35)
plt.show()