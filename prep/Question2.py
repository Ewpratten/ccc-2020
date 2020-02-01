# Question 2: Pretty Average Primes
# Must solve 2N = A + B

import math
MAX_PRIME = 1_000_000

# List of primes to search
primes = []


# Helper for finding possible primes
def findPrimes() -> None:
    marked = [False] * (int(MAX_PRIME / 2) + 100)

    # Find and mark possible primes
    for i in range(1, int((math.sqrt(MAX_PRIME) - 1) / 2) + 1):
        for j in range((i * (i + 1)) << 1,
                       int(MAX_PRIME / 2) + 1, 2 * i + 1):
            marked[j] = True

    # We know 2 is prime
    primes.append(2)

    # Append marked primes
    for i in range(1, int(MAX_PRIME / 2) + 1):
        if (marked[i] == False):
            primes.append(2 * i + 1)


class PAP(object):

    # N
    n: int

    def __init__(self, data: int):
        self.n = data * 2  # Solve 2N

    # Solve Goldbach's conjecture for N
    def exec(self) -> (int, int):

        # Fail on non-solvable
        if (self.n <= 2 or self.n % 2 != 0):
            return (0, 0)

        i = 0
        while (primes[i] <= self.n // 2):

            # Find difference from nearest prime
            diff = self.n - primes[i]

            # Check if the difference is a prime
            if diff in primes:

                # If so, we have found a working set of primes
                return (primes[i], diff)
            i += 1


if __name__ == "__main__":
    # Get the tests count
    tests = int(input())

    # Read data
    data = []
    for _ in range(tests):
        data.append(int(input()))

    # Find possible primes
    findPrimes()

    # Execute calculation for each test case
    for case in data:
        app = PAP(case)

        a, b = app.exec()
        print(f"{a} {b}")
