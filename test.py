def decode(message_file):
    # Read the content of the file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Extract numbers from each line and store them in a list
    numbers = [int(line.split()[0]) for line in lines]

    # Extract corresponding words based on the numbers
    words = [line.split()[1] for line in lines if int(line.split()[0]) in numbers]

    # Join the words into a string and return
    decoded_message = ' '.join(words)
    return decoded_message

# Example usage:
message_file = 'message_file.txt'  # Replace with the actual file name
result = decode(message_file)
print(result)