import sys


def validNumber(n: str) -> bool:
    try:
        int(n)
        return True
    except:
        return False


def findMissingUtil(arr, low, high, diff):

    # Find index of middle element
    mid = int(low + (high - low) / 2)

    if (arr[mid + 1] - arr[mid] != diff):
        return ((arr[mid] + diff), mid)

    if (mid > 0 and arr[mid] -
            arr[mid - 1] != diff):
        return ((arr[mid - 1] + diff), mid - 1)

    if (arr[mid] == arr[0] + mid * diff):
        return (findMissingUtil(arr, mid + 1,
                                high, diff), mid + 1)

    return (findMissingUtil(arr, low,
                            mid - 1, diff). mid - 1)


# def findMissing(arr, n):

#     # Binary search
#     return findMissingUtil(arr, 0, n - 1, int((arr[n - 1] - arr[0]) / n))


if __name__ == "__main__":
    # Build a grid
    grid = []

    # Read input
    for _ in range(3):
        data = input().split(" ")

        # Build the grid
        grid.append([int(c) for c in data if validNumber(c)])

    # Handle each row
    for row in grid:

        # If the row is missing too much info, solve in the Y axis for missing numbers
        if len(row) == 1:
            # TODO: This will not solve the stage 2 of this question
            pass
        elif len(row) == 2:
            val, index = findMissingUtil(row, 0, len(
                row) - 1, int((row[len(row) - 1] - row[0]) / len(row)))

            if index == -1:
                print(val, row[0], row[1])
            elif index == 0:
                print(row[0], val, row[1])
            elif index == 1:
                print(row[0], row[1], val)
        else:
            print(row[0], row[1], row[2])
