
def findJumpsForVal(val: int) -> list:
    pass


# Read the number of lines
line_count = int(input(""))

# We don't need the second input
input("")

# Read all rows of the grid
grid: list = []
while len(grid) < line_count:
    # Add row to the grid
    grid.append([int(i) for i in input("").split(" ")])

# Define a tasks queue for jumps and tracker for visited points
tasks: list = []
visited: list = []

# Push the first position to the tasks list
tasks.append({
    "x": 0,
    "y": 0,
    "value": grid[0][0]
})

# Handle tasks running
while len(tasks) > 0:

    # Pop the first task off the stack
    task: dict
    try:
        task = tasks.pop(0)
    except ValueError as e:
        break

    # Mark this as a visited position
    visited.append((task["x"], task["y"]))

    # Find all allowed jumps
    jumps: list = findJumpsForVal(task["value"])

    # Check all jumps
    for jump in jumps:

        # Jump not valid if we have been there before
        if jump in visited:
            continue

        # If the jump is the end, we have finished
        if jump == ():
            print("yes")
            exit(0)

        # Otherwise, add the jump to the list of points
        tasks.append({
            "x": jump[0],
            "y": jump[1],
            "value": grid[jump[1]][jump[0]]
        })


# If tasks runs out, we can not finish the room
print("no")
