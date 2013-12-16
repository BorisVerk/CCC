infile = open('s1.in', 'r')

#in case given year is unique
year = int(infile.read()) + 1

def next_unique(year):
    for x in str(year):
        if str(year).count(x) > 1:
            return next_unique(year + 1)
    else: return year

print next_unique(year)

infile.close()