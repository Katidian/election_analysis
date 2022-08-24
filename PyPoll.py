# List of the data points we need:
# 1. Total votes cast
# 2. List of all candidates who received votes
# 3. Total votes won by each candidate
# 4. Percentage of total votes won by each candidate
# 5. Election winner based on popular vote (highest percentage of total votes)

# Add dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:


    # To do: read and analyze data

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Print the header row
    headers = next(file_reader)
    print(headers)

    

# THE LONG WAY
# # Use the open statement to open the file as a text file
# outfile = open(file_to_save, "w")

# # Write some data to the text file
# outfile.write("Hello World")

# # Close the file
# outfile.close()

# # # Use the with statement to open the file as a text file
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file
#     # txt_file.write("Arapahoe, ")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson")

#     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")



