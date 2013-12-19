"""testing.py
Developed to test my python problems in preparation for the CCC

Assumptions are
Folder structure:
    year
     senior
      solutions are here as s1.1.in and s1.1.out files
     1.py, 2.py etc
And full path of file must be passed in as argv[1]

Todos:
    Remove second assumption
    Add error support

"""

import sys
import os

if len(sys.argv) != 2:
    sys.exit('Usage: python testing.py /path/to/file/being/tested/X.py')

file_path = sys.argv[-1]
file_directory = sys.argv[-1][:-4]
problem_number = int(file_path[-4])

if file_path[-3:] != '.py' or file_path[-5] != '/' or problem_number not in range(1,5):
    sys.exit('Bad file name. Should be X.py \nwhere x is from 1 to 5')

#this folder layout is a given. folder will contain all .in files and their outs
solutions_directory = file_path[:-4] + 'senior/S' + str(problem_number) + '/'
solution_file_paths = []
for filename in os.listdir(solutions_directory):
    if filename.endswith('.in'):
        infile_path = solutions_directory + filename
        outfile_path = solutions_directory + filename.replace('in', 'out')
        solution_file_paths.append((infile_path, outfile_path))

temp_infile_path = file_directory + 's' + str(problem_number) + '.in'
temp_outfile_path = file_directory + 'progOutput.txt'

trials_failed = 0

for infile_path, outfile_path in solution_file_paths:    
    infile = open(infile_path, 'r')
    outfile = open(outfile_path, 'r')
    
    with open(temp_infile_path, 'w') as temp_in:
        for line in infile:
            temp_in.write(line)
        infile.seek(0)
    
    os.system('python ' + file_path + ' > ' + temp_outfile_path)
    
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
            
    infile.close()
    outfile.close()
    
if trials_failed == 0:
    print '\nComplete Success\n'
else:
    print '\nTrials Failed: ' + str(trials_failed)
    print 'Out of: ' + str(len(solution_file_paths))
os.system('rm -f ' + temp_infile_path + ' ' + temp_outfile_path)