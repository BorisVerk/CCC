import requests
import os

file_dir_url = "http://mmhs.ca/ccc/2014/"

files = {1: ['1', '2', '3', '4', '5'],
         2: ['1a', '1b', '2a', '2b', '3a', '3b', '4a', '4b', '5a', '5b'],
         3: ['1', '2', '3', '4', '5'],
         4: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15'],
         5: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']}

current_directory = os.getcwd()
print 'Downloading input/output files for the 2014 CCC (senior) to', current_directory
print 'Your files will be organized into 5 folders with the names S1, S2, S3, S4, S5'

total_downloaded_files = 0
not_downloaded_files = []

for problem_number, file_numbers in files.iteritems():

    problem_directory = current_directory + '/S' + str(problem_number) + '/'
    if not os.path.exists(problem_directory):
        os.makedirs(problem_directory)

    for file_number in file_numbers:
        infile_name = 's' + str(problem_number) + '.' + file_number + '.in'
        outfile_name = 's' + str(problem_number) + '.' + file_number + '.out'

        infile_url = file_dir_url + infile_name
        outfile_url = file_dir_url + outfile_name

        infile_data = requests.get(infile_url)
        outfile_data = requests.get(outfile_url)

        if 404 in [outfile_data.status_code, infile_data.status_code]:
            not_downloaded_files.append(infile_name)
            not_downloaded_files.append(outfile_name)
        else:

            with open(problem_directory + infile_name, 'w') as infile:
                infile.write(infile_data.text.replace('\r', '')) #the \r messes up my test.py comparison
            with open(problem_directory + outfile_name, 'w') as outfile:
                outfile.write(outfile_data.text.replace('\r', ''))
            total_downloaded_files += 2

print
print 'Downloaded %d files' % total_downloaded_files
if not_downloaded_files:
    print 'The following %d files could not be downloaded (it is probable they just haven\'t been posted yet):' % len(not_downloaded_files)
    print_string = ''
    for file in not_downloaded_files:
        print_string += file + ', '
    print print_string