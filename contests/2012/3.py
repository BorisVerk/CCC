from collections import defaultdict

with open('s3.in') as infile:
    number_of_sensors = int(infile.readline()) #skip first line

    readings = [int(line) for line in infile]

reading_freq = defaultdict(int)
for reading in readings:
    reading_freq[reading] += 1

#the value is a list of readings which have the same frequency
#(the frequency is the key)
most_frequent_readings = defaultdict(list)
for k, v in reading_freq.iteritems():
    most_frequent_readings[v].append(k)

first_most_common = most_frequent_readings.pop(max(most_frequent_readings))
if len(first_most_common) > 1:
    #if some readings share the same largest frequency print the largest possible dif
    #which is obviously going to be the largest value minus the smallest
    print max(first_most_common) - min(first_most_common)
else:
    #otherwise get the next biggest frequency, this could potentialy contain loads of readings
    second_most_common = most_frequent_readings.pop(max(most_frequent_readings))
    #calculate what difference each reading will make with THE most frequent reading
    possible_difs = map(lambda x: abs(first_most_common[0] - x), second_most_common) #you think this is a joke?
    #return the largest dif (as per problem specifications)
    print max(possible_difs)