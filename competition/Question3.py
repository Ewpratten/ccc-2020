import re


def findPerms(first_str, second_str):

    # Handle max recursion
    if not first_str:
        yield second_str
        return
    if not second_str:
        yield first_str
        return

    # Find the first set
    for result in findPerms(first_str[1:], second_str):
        yield first_str[0] + result

    # Find the second set
    for result in findPerms(first_str, second_str[1:]):
        yield second_str[0] + result


# Read the needle
needle: str = input("")

# Read the haystack
haystack: str = input("")

# Find all permutations of the needle
if(len(needle) > 1):
    permutations = list(findPerms(needle[:-1], needle[-1:]))
else:
    permutations = [needle]

# Count the number of occurrences of each permutation
total: int = 0
for permutation in permutations:
    total += 1 if len(re.findall(permutation, haystack)) else 0

print(total)
