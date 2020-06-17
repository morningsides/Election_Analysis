# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Dictionary to hold candiate/vote totals
candidate_totals_dict = {}
candidate_totals_list = []
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

for candidate in candidate_votes:
    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Add items to dictionary then save each dictionary to a list for unpacking later
    candidate_totals_dict = {'candidate': candidate,
                             'votes': votes, 'vote_percentage': vote_percentage}
    candidate_totals_list.append(candidate_totals_dict)

    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate
        winning_percentage = vote_percentage

# Write our file
with open(file_to_save, 'w') as election_file:
    election_file.write("Election Results\n")
    election_file.write(20 * "-" + "\n")
    election_file.write(f'Total Votes: {total_votes:,}\n')
    election_file.write(20 * "-" + "\n")

    for item in candidate_totals_list:
        election_file.write(
            f"{item['candidate']}: {item['vote_percentage']:.1f}% ({item['votes']:,}) \n")
    election_file.write(20 * "-" + "\n")
    election_file.write(f"Winner: {winning_candidate}\n")
    election_file.write(f"Winning Vote Count: {winning_count:,}\n")
    election_file.write(f"Winning Percentage: {winning_percentage:.1f}%\n")
    election_file.write(20 * "-" + "\n")
