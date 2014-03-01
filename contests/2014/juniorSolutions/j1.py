def which_triangle_type(angles):
    if sum(angles) is not 180:
        return 'Error'
    for angle in angles:
        if angles.count(angle) == 3:
            return 'Equilateral'
        if angles.count(angle) == 2:
            return 'Isosceles'
    return 'Scalene'

angles = [int(raw_input()) for _ in range(3)]
print which_triangle_type(angles)