#started first two problems at 618
with open('s1.in', 'r') as infile:
    text = infile.read().lower()
    if text.count('t') > text.count('s'):
        print 'English'
    else:
        print 'French'
