def read_file(filename):
    """Reads the lines of a file and returns them as a list."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            return [line.strip() for line in lines]  # Remove newline characters
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
        return None


def navigate_lines():
    """Prompts the user to navigate the lines of a file."""
    filename = input("Enter filename: ")
    lines = read_file(filename)

    if lines is not None:  # Check if file was successfully read
        while True:
            print(f"The file has {len(lines)} line(s). (Enter 0 to quit)")
            try:
                line_number = int(input("Enter line number (1 to number of lines): "))
                if line_number == 0:  # Quit condition
                    print("Exiting the program. Goodbye!")
                    break
                elif 1 <= line_number <= len(lines):  # Valid line number
                    print(f"Line {line_number}: {lines[line_number - 1]}")
                else:
                    print("Invalid line number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    navigate_lines()
