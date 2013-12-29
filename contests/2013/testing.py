#!/usr/bin/env python

"""testing.py
Developed to test my python problems in preparation for the CCC

Assumptions are
Folder structure:
    year
     senior
      solutions are here as s1.1.in and s1.1.out files
     1.py, 2.py etc

Todos:
    Add error support

"""

import os
import sys

def get_slutions_files(dir):
    file_paths = list()
    for file in os.listdir(dir):
        if file.endswith('.in'):
            infile_path = dir + file
            outfile_path = dir + file.replace('in', 'out')
            file_paths.append((infile_path, outfile_path))
    return file_paths

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
    

problem_number = parse_argv()

current_dir = os.getcwd() + '/'
exec_path = current_dir + str(problem_number) + '.py'

solutions_directory = current_dir + 'senior/S' + str(problem_number) + '/'
solution_file_paths = get_slutions_files(solutions_directory)

temp_infile_path = current_dir + 's' + str(problem_number) + '.in'
temp_outfile_path = current_dir + 'progOutput.txt'


temp_infile_path = current_dir + 's' + str(problem_number) + '.in'
temp_outfile_path = current_dir + 'progOutput.txt'

trials_failed = 0
for infile_path, outfile_path in solution_file_paths:    
    with open(infile_path, 'r') as infile:
        with open(outfile_path, 'r') as outfile:
            with open(temp_infile_path, 'w') as temp_in:
                for line in infile:
                    temp_in.write(line)
                infile.seek(0)
            
            os.system('python ' + exec_path + ' > ' + temp_outfile_path)
            
            with open(temp_outfile_path, 'r') as temp_out:
                actual_output = temp_out.read().strip()
                expected = outfile.read().strip()
                if actual_output != expected:
                    trials_failed += 1
                    print '\nInput:\n' + infile.read().strip()
                    print 'Expected:\n' + expected
                    print 'Actual Output:\n' + actual_output
                    print 'Files: ' + infile_path + ' ' + outfile_path
                    raw_input('\nPress the \'Any\' key to continue.')
    
if trials_failed == 0:
    print '\nComplete Success\n'
else:
    print '\nTrials Failed: ' + str(trials_failed)
    print 'Out of: ' + str(len(solution_file_paths))
os.system('rm -f ' + temp_infile_path + ' ' + temp_outfile_path)