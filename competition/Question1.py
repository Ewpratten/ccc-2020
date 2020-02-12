
# Determine the # of observations
observation_count = int(input(""))

# Get all observations
observations = []
while len(observations) < observation_count:
    # Read & parse line
    observations.append([int(i) for i in input("").split(" ")])

# Sort by time
observations.sort(key=lambda x: x[0])

# Find the longest time step
max_step: float = 0.0
for i in range(len(observations) - 1):

    # find dt
    dt: float = observations[i + 1][0] - observations[i][0]

    # Find difference in distance
    dd: float = observations[i + 1][1] - observations[i][1]

    # Find dist/time
    step: float = abs(dd/dt)

    # Find if step is max
    max_step = max(max_step, step)

print(max_step)
