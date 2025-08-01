# python_tutorial
These are some basic python functions. 
Basic Python commands are fundamental building blocks for writing programs. Here are some of the most commonly used ones:
1. Output:
print(): Used to display output to the console.
>Python    ``print("Hello, World!")``
2. Input:
input(): Used to get user input from the console. The input is always read as a string.
>Python 
``name = input("Enter your name: ")
    print("Hello, " + name + "!")``
3. Data Type Operations:
type(): Returns the type of an object.
>Python
    ``x = 10
    print(type(x)) 
    # Output: <class 'int'>``
    
len(): Returns the number of items in an object (e.g., string, list, tuple, dictionary).
>Python
    ``my_list = [1, 2, 3]
    print(len(my_list))`` 
    
    # Output: 3
int(), float(), str(), bool(): Used for type conversion.
>Python
    num_str = "123"
    num_int = int(num_str)
4. Control Flow:
if, elif, else: Used for conditional execution.
>Python
    ``age = 20
    if age >= 18:
        print("Adult")
    else:
        print("Minor")``

for: Used for iterating over sequences (e.g., lists, strings, ranges).
>Python

``for i in range(5):
        print(i)``

while: Used for looping as long as a condition is true. 
>Python
    ``count = 0
    while count < 3:
        print(count)
        count += 1``

5. List Operations:
append(): Adds an element to the end of a list.
>Python
    ``my_list = [1, 2]
    my_list.append(3) # my_list is now [1, 2, 3]``

insert(): Inserts an element at a specified position.
>Python
    ``my_list.insert(0, 0) # my_list is now [0, 1, 2, 3]``

remove(): Removes the first occurrence of a specified value.
>Python
    ``my_list.remove(2) # my_list is now [0, 1, 3]``

6. Modules:
import: Used to import modules and access their functionalities.
>Python
``import math
print(math.sqrt(16))``

``# Output: 4.0``