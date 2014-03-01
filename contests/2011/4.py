with open('s4.in', 'r') as infile:
    blood = [int(x) for x in infile.readline().split(' ')]
    patients = [int(x) for x in infile.readline().split(' ')]

#for reference
types = ['O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+']


def take_blood(patient, blood_type):
    units_taken = min(blood[blood_type], patients[patient])
    patients[patient] -= units_taken
    blood[blood_type] -= units_taken
    return units_taken

total = 0

#everyone takes whatever blood type they have
for x in range(8):
    total += take_blood(x, x)

# O+ takes left over O-
total += take_blood(1, 0)

# A- takes O-
total += take_blood(2, 0)

# A+ takes O+ and A- and O-
total += take_blood(3, 1) + take_blood(3, 2) + take_blood(3, 0)

# B- takes O-
total += take_blood(4, 0)

# B+ takes O+ and B- and O-
total += take_blood(5, 1) + take_blood(5, 4) + take_blood(5, 0)

# AB- can accept everything negative
for x in range(0, 8, 2):
    total += take_blood(6, x)

# AB+ can accept everything
for x in range(8):
    total += take_blood(7, x)

print total