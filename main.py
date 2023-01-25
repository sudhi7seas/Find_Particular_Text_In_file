from pathlib import Path

files_dir = Path('files')

file_type = files_dir.glob('**/*.txt')
print(file_type)
word = 'Failed'
for files in file_type:
  print(files)

  with open(files, 'r') as file:
    lines = file.readlines()
    print(lines)
   
    for index, Line in enumerate(lines):
      if Line.find(word) != -1:
        print(word, 'string present in a file')
        print('Line number:', index)
        print('Line', Line)
  

