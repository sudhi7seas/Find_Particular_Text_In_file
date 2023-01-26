# To represent file paths by proper Path objects pathlib has been used
from pathlib import Path

# Import datetime module so that the it could be used as an attribute for log file generation with current date and time
from datetime import datetime as dt

# To store the file path , a new variable 'files_dir' has been created
files_dir = Path('files')

# Returns a list of files that matches the path specified in the function argument
file_type = files_dir.glob('**/*.*')

# To get the results in a log that is generated with the current date time and hence here 'dt.now().strftime('Y-%m-%d.%H-%M-%S')' has been used
filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.LOG"

# To search for the string 'Failed' in all the files present in a directory
word = 'Failed'

# Loop through all the files
for files in file_type:

  # Open the files in read-only and read the lines.
  with open(files, 'r') as file:
    lines = file.readlines()

    # Loop through each line of the file and if there exists a 'Failed' string then print it in a log file
    for index, Line in enumerate(lines):
      if Line.find(word) != -1:
        with open(filename, 'a') as file:
          print('Location of the file that inclues a failed string', files, file=file)
          print('String present in a file :', word, file=file)
          print('Index id of the Failed string is present:', index, file=file)
          print('\n', file=file)