# Practice with F-Strings

population = {'India': 1419316933, 'China': 1407181209, 'United States': 342034432, 'Indonesia': 283587097, 'Pakistan': 257047044}

print("Top 5 Largest Populations by Country:\n")
for index, country in enumerate(population.keys(), start=1):
    print(f"{index:2d} {country:<15s} {population[country]:>15,}")
# original: print(f"{index:2d} {country:<15s} {population[country]:15.0f,}")

# 'population = {...}' is a variable that stores a dictionary containing keys (string of country names) & values (integers).
#                      purpose: stores key pairs for later use.
#                      example: population['China'] returns 1407181209

# 'population.keys()'  Returns a list-like object of the dictionary's keys

# 'index'
# 'index:2d'           2d formats the index as an integer (d) with a minimum width of 2 characters.
#                      example: 1 becomes 1 (padded with leading space

# 'enumerate(..., start=1)'
#                      generates pairs of 'index, key' where index starts at 1
#                      purpose: iterates over the dictionary keys & assigns an index to each.

# 'country:<15s'       Left aligns (<) the country name (s is for string) in a field of 15 characters.
#                      example: 'India' becomes 'India' with 11 spaces added

# 'population[country]:15.0f'
#                      15.0f formats the population as a float (f) with 0 decimal places (.0)
#                      15 is the width of characters, adjusted to the largest number on the dataset

# 'population[country]:>15,'
#                      In this improved version, the integers are aligned to the right
#                      commas are added for readability (thousand separators)