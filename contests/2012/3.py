#took too long to make, takes too long to run, 
#improve me
#some of these conversions must be completely unnecessary
#I hate this code.

import collections

def parse_sensors():
    sensors = []    
    with open('/Users/HDD/src/CCC/contests/2012/s3.in', 'r') as infile:
        infile.readline() #skip first line
        for line in infile:
            sensors.append(int(line))
    return sensors
        
sensors = parse_sensors()

sensor_count = {}
for reading in set(sensors):
    count = sensors.count(reading)
    sensor_count[reading] = count


count_sensors = collections.defaultdict(list)
for (k, v) in sensor_count.items():
    count_sensors[v].append(k)

#this is a function because returns are really easy
def get_answer(count_sensors):
    most_common_reading = count_sensors.pop(max(count_sensors.keys()))
    if len(most_common_reading) > 1:
        most_common_reading = sorted(most_common_reading)
        return abs(most_common_reading[0] - most_common_reading[-1])
    else:
        second_most_common_reading = count_sensors.pop(max(count_sensors.keys()))
        if second_most_common_reading > 1:
            max_dif = 0
            for reading in second_most_common_reading :
                dif = abs(most_common_reading[0] - reading)
                if dif > max_dif:
                    max_dif = dif
            return max_dif
        else: return abs(most_common_reading[0] - second_most_common_reading[0])
        

print get_answer(count_sensors)