#not my solution
with open("s5.in", 'r') as infile:
    number = int(infile.readline().strip())
 
cost = 0

while number != 1:
    max_factor = int(number**0.5) + 1
    for factor in range(2, max_factor): 
        if number % factor == 0: 
            x = number / factor
            number -= x
            cost += number / x 
            break
    else: # if number is prime, go back only 1
        number -= 1
        cost += number
        
print cost