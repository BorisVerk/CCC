def rtod(roman_digit):
    #returns a decimal interger converted from a roman digit
    #works for range of unus (I) (1) to mille (M) (1000)
    conversions = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000}
    return conversions.get(roman_digit.upper(), None)

def atod(aromatic_digit):
    #returns a decimal int from aromatic digits
    return int(aromatic_digit[0]) * rtod(aromatic_digit[-1])

with open('s2.in', 'r') as infile:
    aromatic = infile.readline().strip()
    parsed_aromatic = [aromatic[x:x+2] for x in range(0, len(aromatic), 2)]

decimal = []
for aromatic_digit in parsed_aromatic:
    decimal_digit = atod(aromatic_digit)
    decimal.append(decimal_digit)
    
aromatic_bases = [rtod(aromatic_digit[1]) for aromatic_digit in parsed_aromatic]

for x in range(0, len(aromatic_bases)-1):
    if aromatic_bases[x] < aromatic_bases[x+1]:
        decimal[x] *= -1

print sum(decimal)