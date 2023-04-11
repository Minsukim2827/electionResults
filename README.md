# Election Results Analyzer
This is a Python program to analyze the election results by reading a CSV file with party-wise vote counts and displaying the results in the form of a bar chart.

## Features
Reads a CSV file with party-wise vote counts
Calculates the total number of votes and seat allocation for each party
Displays the results in the form of a bar chart
Prints the party-wise vote count and seat allocation
Usage
Clone the repository:
```
git clone https://github.com/<username>/election-results-analyzer.git
```
Navigate to the project directory:
```
cd election-results-analyzer
```
Run the program:
```
python3 election_results_analyzer.py
```
Enter the file path and name of the CSV file with the party-wise vote counts when prompted.

The program will display the party-wise vote count and seat allocation, as well as a bar chart of the results.

## Dependencies
This program requires the following libraries to be installed:

numpy
matplotlib
You can install these libraries using the following command:

```
pip3 install numpy matplotlib
```
## File format
The CSV file should contain two columns: the name of the party and the number of votes received by the party. The first row of the CSV file should contain the header.

Example CSV file:

```
Party,Votes
Party A,10000
Party B,20000
Party C,15000
Party D,3000
```
