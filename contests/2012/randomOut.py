#!/usr/bin/env python

"""
randomOut.py
provides random in file in the working directory
for easier testing when actually writting the program
"""

import os
import sys
import random
random.seed()

def parse_argv():
    if len(sys.argv) != 2:
        sys.exit("Usage: python ./test.py problem_number")

    problem_number = 0
    if len(sys.argv[-1]) == 1: problem_number = int(sys.argv[-1])
    elif len(sys.argv[-1]) == 4 and sys.argv[-1][1:] == ".py":
        try: problem_number = int(sys.argv[-1][0])
        except ValueError:
            sys.exit("Usage: python ./test.py problem_number")
    else: sys.exit("Usage: python ./test.py problem_number")
    
    if problem_number not in range(1,6): 
        sys.exit("Bad File Name: there are only 5 problems")
        
    return problem_number
    
def get_rand_solution_file_paths(directory):
    file_paths = list()
    for file in os.listdir(directory):
        if file.endswith('.in'):
            infile_path = directory + file
            outfile_path = directory + file.replace('in', 'out')
            file_paths.append((infile_path, outfile_path))
    return random.choice(file_paths)

def copyfile(source, dest):
    for line in source:
        dest.write(line)

problem_number = parse_argv()

current_dir = os.getcwd() + '/'

solutions_directory = current_dir + 'senior/S' + str(problem_number) + '/'

input_file, output_file = get_rand_solution_file_paths(solutions_directory)

new_input_file = current_dir + 's' + str(problem_number) + '.in'

with open(input_file, "r") as original_input:
    with open(new_input_file, "w") as new_input:
        copyfile(original_input, new_input)
        
with open(output_file, "r") as original_output:
    print "Output should be:"
    for line in original_output:
        print line