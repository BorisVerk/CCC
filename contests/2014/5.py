def what_does_the_fox_say():
    return 'YIP YIPIAAIIAIAPYIYIYPIAAIYAIAIYYAA'

def what_does_the_fox_eat(points):


total_positions = int(raw_input())
points = []

for _ in xrange(total_positions):
    x, y = map(int, raw_input().split(' '))
    points.append((x, y))

print what_does_the_fox_eat(points)