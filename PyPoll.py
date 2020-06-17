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
# County options and candidate votes
county_options = []
county_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Dictionary/list to hold candiate/vote totals
candidate_totals_dict = {}
candidate_totals_list = []
# Dictionary/list to hold county/vote totals
county_totals_dict = {}
county_totals_list = []

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
        # Get the counties for each row
        county_name = row[1]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # If county not in county_options list add it
        if county_name not in county_options:
            # Add the county name to the county_options list.
            county_options.append(county_name)
            # And begin tracking that counties voter count.
            county_votes[county_name] = 0
        # Add a vote to that counties count
        county_votes[county_name] += 1

# Find candidate totals, create candidate objects
for candidate in candidate_votes:
    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Add items to dictionary then save each dictionary to a list for unpacking later
    candidate_totals_dict = {'candidate': candidate,
                             'votes': votes,
                             'vote_percentage': vote_percentage}
    candidate_totals_list.append(candidate_totals_dict)

    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate
        winning_percentage = vote_percentage

# Find out the county totals, create county objects
for county in county_votes:
    # Retrieve vote count and percentage.
    votes = county_votes[county]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Add items to dictionary then save each dictionary to a list for unpacking later
    county_totals_dict = {'county': county,
                          'votes': votes,
                          'vote_percentage': vote_percentage}
    county_totals_list.append(county_totals_dict)

    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_county_votes = votes
        winning_county = county
        winning_percentage_county = vote_percentage

# Write our file and demonstrate that we are masters of string interpolation
with open(file_to_save, 'w') as election_file:
    election_file.write("Election Results\n")
    election_file.write(20 * "-" + "\n")
    election_file.write(f'Total Votes: {total_votes:,}\n')
    election_file.write(20 * "-" + 2 * "\n")

    election_file.write('County Votes: \n')
    for item in county_totals_list:
        election_file.write(
            f"{item['county']}: {item['vote_percentage']:.1f}% ({item['votes']:,}) \n")
    election_file.write("\n")
    election_file.write(20 * "-" + "\n")
    election_file.write(f"Largest County Turnout: {winning_county}\n")
    election_file.write(20 * "-" + "\n")
    for item in candidate_totals_list:
        election_file.write(
            f"{item['candidate']}: {item['vote_percentage']:.1f}% ({item['votes']:,}) \n")
    election_file.write(20 * "-" + "\n")
    election_file.write(f"Winner: {winning_candidate}\n")
    election_file.write(f"Winning Vote Count: {winning_count:,}\n")
    election_file.write(f"Winning Percentage: {winning_percentage:.1f}%\n")
    election_file.write(20 * "-" + "\n")

# Print our file to terminal
with open(file_to_save, 'r') as election_file:
    for line in election_file:
        print(line, end='')
