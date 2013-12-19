with open('s1.in', 'r') as infile:
    year = int(infile.read()) + 1#in case given year is unique

def next_unique(year):
    for digit in str(year):
        if str(year).count(digit) > 1:
            return next_unique(year + 1)
    else: return year

print next_unique(year)