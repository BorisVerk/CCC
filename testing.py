#!/usr/bin/env python

"""testing.py
Developed to test my python problems in preparation for the CCC

Assumptions are
all programs being tested are called X.py where X is the problem number (from 1 to 5)
Folder structure:
    year
     senior
      solutions are here as s1.1.in and s1.1.out files
     1.py, 2.py etc
all files read from sX.in, where X is the problem number

works on at least python 2.6
"""

import os
import sys

def parse_argv():
    if len(sys.argv) != 2:
        sys.exit("Usage: python ./test.py problem_number")

    # it is optional to specify the ".py", otherwise the last argv sould just be the problem number (just one digit)
    if len(sys.argv[-1]) != 1 and sys.argv[-1][1:] != ".py":
        sys.exit("Usage: python ./test.py problem_number")

    problem_number = 0
    try:
        problem_number = int(sys.argv[-1][0])
    except ValueError:
        sys.exit("Usage: python ./test.py problem_number")

    if problem_number not in range(1,6): 
        sys.exit("Bad File Name: there are only 5 problems")
        
    return problem_number

def check_executable(file_path):
    if not os.path.exists(file_path):
        file_name = os.path.basename(file_path)
        sys.exit("Error: file '" + file_name + "' does not exist at " + os.path.dirname(file_path))


def get_solution_file_paths(directory):
    file_paths = []
    for file in os.listdir(directory):
        if file.endswith('.in'):
            infile_path = directory + file
            outfile_path = directory + file.replace('.in', '.out')
            if os.path.exists(outfile_path):
                file_paths.append((infile_path, outfile_path))
            else: 
                sys.exit("Missing out file for " + os.path.basename(infile_path))
    if file_paths:
        return file_paths
    else: sys.exit("No input/output files were found at " + directory)


def copyfile(source, destination):
    for line in source:
        destination.write(line)
    source.seek(0)

    
def report(infile, expected_output, actual_output, infile_path):

    program_input = infile.read().strip()
    if len(program_input) < 200:
        print 'Input:\n' + program_input
    else:
        print 'Program input too long to display'

    print 'Expected:\n' + expected_output
    print 'Actual Output:\n' + actual_output

    infile = os.path.basename(infile_path)
    outfile = infile.replace('in', 'out')
    print 'Files: ' + infile + ' ' + outfile 

    raw_input('Press the \'Any\' key to continue.\n')

def test_program(exec_path, solution_file_paths, temp_infile_path, temp_outfile_path):

    trials_failed = 0

    for infile_path, outfile_path in solution_file_paths:    
        with open(infile_path, 'r') as infile:
            with open(outfile_path, 'r') as outfile:                
                with open(temp_infile_path, 'w') as temp_in:
                    copyfile(infile, temp_in)
                
                os.system('python ' + exec_path + ' > ' + temp_outfile_path)
                
                with open(temp_outfile_path, 'r') as temp_out:
                    actual_output = temp_out.read().strip()
                    expected_output = outfile.read().strip()
                    if actual_output != expected_output:
                        trials_failed += 1
                        report(infile, expected_output, actual_output, infile_path)

    total_trials = len(solution_file_paths)
    if trials_failed:
        print '\nTrials Failed: ' + str(trials_failed)
        print 'Score: %d/%d' % (total_trials-trials_failed, total_trials)
    else:
        print 'Complete Success'
        print 'Score: %d/%d' % (total_trials, total_trials)

    
if __name__ == 'main':
    problem_number = parse_argv()

    current_dir = os.getcwd() + '/'

    exec_path = current_dir + str(problem_number) + '.py' 

    #check that the file we're going to be running actually exists
    check_executable(exec_path)

    solutions_directory = current_dir + 'senior/S' + str(problem_number) + '/'
    solution_file_paths = get_solution_file_paths(solutions_directory)

    temp_infile_path = current_dir + 's' + str(problem_number) + '.in'
    temp_outfile_path = current_dir + 'progOutput.txt'

    try:
        test_program(exec_path, solution_file_paths, temp_infile_path, temp_outfile_path)
    finally:
        os.system('rm -f ' + temp_infile_path + ' ' + temp_outfile_path)