# File handling: reading, writing, appending, binary files
print('File Structure')
print('File operations')

# Asking user for file input
file_name = input('Enter the file name: ')

# Reading from a file
try:
    with open(file_name, 'r', encoding='UTF-8', errors='ignore') as file:
        print(file.read())
except FileNotFoundError:
    print('File not found. Please check the file name')

# Reading a binary file
with open('book_record.xlsx', 'rb', errors='ignore') as file:
    print(file.read())

# Writing to a file
with open('file.md', 'w') as file:
    file.write('This is PLP')

# Appending to a file
with open('file.md', 'a') as file:
    file.write('\nWelcome to PLP')





