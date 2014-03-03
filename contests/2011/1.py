with open('s1.in', 'r') as infile:
    text = infile.read().lower() #lowercase all the letters for easier counting

if text.count('t') > text.count('s'):
    print 'English'
else:
    print 'French'
