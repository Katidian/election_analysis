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

# Initialize total vote counter
total_votes = 0

# Create a candidate options list
candidate_options =[]

# Declare an empty dictionary for candidate votes
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    
    # Read the header row
    headers = next(file_reader)
    
    # Count each row of data after the headers as one vote
    for row in file_reader:
        total_votes += 1

        # Get the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list if it's not already in there
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            # Start tracking the candidate's vote count
            candidate_votes[candidate_name] = 0
        
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")

    print(election_results, end="")
    
    txt_file.write(election_results)

    ## Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
    for candidate in candidate_votes:
        
        # Retrieve candidate's vote count
        votes = candidate_votes[candidate]

        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # Variable for the candidate name and percentage of votes
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)

        txt_file.write(candidate_results)

        ## Determine winning vote count and candidate
        # Determine if the vote count is greater than the current winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If so, the votes count we're on becomes the winning count (and so on)
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n")

    print(winning_candidate_summary)

    txt_file.write(winning_candidate_summary)
    






