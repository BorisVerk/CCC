#doesn't work

#starting grid
sgrid = ['00000',
         '10000',
         '11000',
         '10000',
         '00000']

def is_crystal(magnification, x, y):
    if magnification == 1:
        return bool(int(sgrid[x][y])) #mini hack
    else:
        magnification -= 1
        x = x % (5 ** magnification)
        y = y % (5 ** magnification)
        return is_crystal(magnification, x, y)

with open('s3.in', 'r') as infile:
    infile.readline() #skip first line
    for line in infile:
        magnification, x, y = [int(i) for i in line.split(' ')]
        if is_crystal(magnification, x, y):
            print 'crystal'
        else:
            print 'empty'
