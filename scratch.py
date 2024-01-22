def decode(message_file: str) -> str:
  # Read the content of the file
  with open(message_file, "r") as f:
    lines = f.readlines()
    
    # Sort the lines based on the number assiciated with each word
    ls = [line.split() for line in lines]
    ls.sort(key=lambda x: int(x[0]))
    
    # Extract the last words from the pyramid and store them in a list
    step = 2
    words = []
    i = 0
    while i < len(ls):
      words.append(ls[i][-1])
      i += step
      step += 1
    
    
    # Join the words into a string and return
    return " ".join(words).lower()


# Example usage:
if __name__ == "__main__":
  print(decode("message_file.txt"))
    
    