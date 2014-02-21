#!/usr/bin/env python

import os, sys

current_dir = os.getcwd()
test_suite_path = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(test_suite_path)
import testing


problem_number = testing.parse_argv()

current_dir = os.getcwd() + '/'

exec_path = current_dir + str(problem_number) + '.py' 

testing.check_executable(exec_path)

solutions_directory = current_dir + 'senior/S' + str(problem_number) + '/'
solution_file_paths = testing.get_solution_file_paths(solutions_directory)

temp_infile_path = current_dir + 's' + str(problem_number) + '.in'
temp_outfile_path = current_dir + 'progOutput.txt'

try:
    testing.test_program(exec_path, solution_file_paths, temp_infile_path, temp_outfile_path)
finally:
    os.system('rm -f ' + temp_infile_path + ' ' + temp_outfile_path)