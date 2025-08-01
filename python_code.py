
# This is a simple Python script that prints a greeting message
print('Hello Everybody!')
print('This is a simple Python script.')

# This is a simple Python script that performs basic arithmetic operations
# It defines a function to add, subtract, multiply, and divide two numbers
def simple_calcs(a, b):
    add = a + b
    subtract = a - b
    times = a * b
    divide = a / b
    return f'Addition: {add}, Subtraction: {subtract}, Times: {times}, Division: {divide}'
def power_calc(a, b):
    return a ** b

# Performing the calculations and storing in variables. 
calculations = simple_calcs(10,20)
new_power = power_calc(10,2)    

# Printing the results of the calculations
print(f'The simple calculations of 10 and 20 are : \n{calculations}')
print(f'The power of 10 raised to 2 is: {new_power}')
print('This is a simple Python script. \nI hope you find it useful!')
