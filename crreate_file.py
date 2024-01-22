import os

def create_file():
    # read input from user
    user_input = input("Enter problem name: ")
    
    directory_name = user_input
    file_name = "-".join([i.lower() for i in user_input.split(" ")]) + ".cpp"
    
    # create directory
    os.mkdir(directory_name)
    
    # create file
    path = os.path.join(directory_name, file_name)
    f = open(path, "w")
    f.write("#include <bits/stdc++.h>\n\nusing namespace std;\n")
    
    f.close()
    
    
if __name__ == "__main__":
    create_file()