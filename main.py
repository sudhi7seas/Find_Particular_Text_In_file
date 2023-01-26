# To represent file paths by proper Path objects pathlib has been used
from pathlib import Path

# To store the file path , a new variable 'files_dir' has been created
files_dir = Path('files')

# Returns a list of files that matches the path specified in the function argument
file_type = files_dir.glob('**/*.txt')

# To search for the string 'Failed' in all the files present in a directory
word = 'Failed'

# Loop through all the files
for files in file_type:

  # Open the files in read-only and read the lines.
  with open(files, 'r') as file:
    lines = file.readlines()

    # Loop through each line of the file and if there exists a 'Failed' string then print it in a 'Result.txt' file
    for index, Line in enumerate(lines):
      if Line.find(word) != -1:
        with open('Result.txt', 'a') as file:
          print('Location of the file that inclues a failed string', files, file=file)
          print('String present in a file :', word, file=file)
          print('Index id of the Failed string is present:', index, file=file)
          print('\n', file=file)