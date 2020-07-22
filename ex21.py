def add(a,b):
    print(f'Adding {a}+{b}')
    return a + b

def subtract(a,b):
    print(f'subtracting {a} - {b} ')
    return a - b

def multiply(a,b):
    print(f'multipling {a} * {b}')
    return a * b

def divide(a,b):
    print(f'dividing {a} / {b}')
    return a / b

print("Let's do some math with just function!")

age = add(30,5)
height = subtract(78, 4)
weight = multiply (90, 2)
iq = divide(180, 2)

print("age:"+ str(age) + "height:" + str(height) + "weight:" + str(weight) + "iq:" + str(iq))

# A puzzle  
print('here is a puzzle.')

what_is = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ",what_is,"can you do it by hand ?")
