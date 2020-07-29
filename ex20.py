from sys import argv

script, input_file = argv

def print_all(f): # see 18
    print(f.read())

def rewind(f):  # see 22 to 33
    f.seek(0)

def print_a_line(line_count, mark, f):  # from 27
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("\n Now let's rewind, kind of like a tape.")

rewind(current_file)

print("\n Let's print three lines:\n")

current_line = 1
colon = " : "
print_a_line(current_line, colon, current_file)

current_line = current_line + 1
print_a_line(current_line, colon, current_file)

current_line = current_line + 1
print_a_line(current_line, colon, current_file)
