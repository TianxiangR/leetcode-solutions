import os

def generate_file_from_problem_name(name: str, extension: str):
    tokens = name.split('.')
    problem_num = tokens[0]
    rest = tokens[1].strip()
    rest = rest.lower()
    rest = rest.replace(' ', '-')
    rest = rest.replace('\'', '-')
    file_name = problem_num + '.' + rest + '.' + extension
    
    with open(file_name, 'w') as file:
      pass
    
  
if __name__ == '__main__':
  name = input('Problem Name: ')
  extension = input('Extension: ')
  
  generate_file_from_problem_name(name, extension)
  