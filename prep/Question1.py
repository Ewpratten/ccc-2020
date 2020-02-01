# Question 1: Flipper


class Flipper(object):

    # Tracker for instructions
    instructions: list

    def __init__(self, data: str):

        # Parse data into an instruction set
        self.instructions = [c for c in data.strip()]

    def exec(self):

        # Count each operation
        counts = {
            "horizontal": len([c for c in self.instructions if c is "H"]),
            "vertical": len([c for c in self.instructions if c is "V"]),
        }

        # Define an output
        output = [[1, 2], [3, 4]]

        # If there are an odd number of either operation, execute it
        if counts["horizontal"] % 2 is 1:
            output = [output[1], output[0]]
        if counts["vertical"] % 2 is 1:
            output = [[output[0][1], output[0][0]],
                      [output[1][1], output[1][0]]]

        # STRFMT the output
        return f"{output[0][0]} {output[0][1]}\n{output[1][0]} {output[1][1]}"


if __name__ == "__main__":
    data = input()
    app = Flipper(data)
    print(app.exec())
