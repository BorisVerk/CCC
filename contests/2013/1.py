def next_unique(year):
    for digit in str(year):
        if str(year).count(digit) > 1:
            return next_unique(year + 1)
    else: return year

with open('s1.in', 'r') as infile:
    year = int(infile.read()) + 1 #the +1 is in case given year is unique
print next_unique(year) 