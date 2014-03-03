#unfinished
with open('s5.in', 'r') as infile:
    infile.readline() #dont need the first line
    remaining_file_lines = infile.read().split('\n')
    switches = [bool(int(x)) for x in remaining_file_lines]

