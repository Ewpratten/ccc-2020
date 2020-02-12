
# Read treat params
S: int = int(input(""))
M: int = int(input(""))
L: int = int(input(""))

# Print the approperate mood
print("happy" if (1*S+2*M+3*L) >= 10 else "sad")