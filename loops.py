# counties_tuple = ("Arapahoe", "Denver", "Jefferson")
# for county in counties_tuple:
#     print(county)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")


# voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
#                {"county": "Denver", "registered_voters": 463353},
#                {"county": "Jefferson", "registered_voters": 432438}]


# for county_dict in voting_data:
#     print(county_dict['registered_voters'])

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# # for county, value in counties_dict.items():
# #     print(f"{county} county has {value} registered volters.")
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters:,} registered voters.")


voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
               {"county": "Denver", "registered_voters": 463353},
               {"county": "Jefferson", "registered_voters": 432438}]

for i in range(len(voting_data)):
    print(
        f'{voting_data[i]["county"]} county has {voting_data[i]["registered_voters"]:,} registered voters.')
