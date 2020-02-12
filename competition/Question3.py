## Itertools SRC ##
def pm(iterable):
    pool = tuple(iterable)
    n = len(pool)
    r = n
    
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])

    # Tracker for duplicates
    seen = set()
    seen.add(tuple(pool[i] for i in indices[:r]))

    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]

                pm_str = tuple(pool[i] for i in indices[:r])
                if not (pm_str in seen or seen.add(pm_str)):
                    yield pm_str
                break
        else:
            return

## Main Program ##


# Read the needle
needle: str = input("")

# Read the haystack
haystack: str = input("")

# Count the number of occurrences of each permutation
total: int = 0
for permutation in pm(needle):

    # Check for occurrences of the permutation
    if ''.join(permutation) in haystack:
        total += 1

print(total)
