#Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
#range of 1 to 25.
def get_odd_numbers():
    odd_numbers = [number for number in range(1, 26) if number % 2 != 0]
    return odd_numbers

# Call the function and print the result
result = get_odd_numbers()
print(result)

#Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
#to demonstrate their use.
'''`*args` and `**kwargs` are used in Python functions to allow the passing of a variable number of arguments.

- `*args` allows a function to accept any number of positional arguments. The `*args` syntax allows you to pass a variable number of arguments to a function. These arguments are collected into a tuple.

- `**kwargs` allows a function to accept any number of keyword arguments. The `**kwargs` syntax allows you to pass a variable number of keyword arguments to a function. These arguments are collected into a dictionary.

Here's an example demonstrating the use of `*args` and `**kwargs` in functions:'''


# Function using *args
def print_args(*args):
    for arg in args:
        print(arg)

# Function using **kwargs
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Demonstrate *args
print("Using *args:")
print_args(1, 2, "three", [4, 5])

# Demonstrate **kwargs
print("\nUsing **kwargs:")
print_kwargs(name="John", age=25, city="New York")


'''In the `print_args` function, `*args` allows you to pass any number of positional arguments, and they are printed inside the function.

In the `print_kwargs` function, `**kwargs` allows you to pass any number of keyword arguments, and they are printed as key-value pairs inside the function.'''


'''Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
16, 18, 20].

In Python, an iterator is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__(). An iterator must have these methods to be considered iterable.

__iter__() initializes the iterator object and returns it.
__next__() returns the next element in the sequence. When there are no more elements, it should raise the StopIteration exception.
Here's an example using the iterator protocol to print the first five elements of the given list:'''

my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Create an iterator object
my_iterator = iter(my_list)

# Iterate and print the first five elements
for _ in range(5):
    print(next(my_iterator))

'''Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator
function.'''

In Python, a generator function is a special kind of function that allows you to iterate over a potentially large sequence of data without creating the entire sequence in memory at once. It uses the yield keyword to produce a series of values in a lazy, on-demand fashion. The state of the generator function is maintained between successive calls to yield.

The yield keyword is used to pause the execution of the generator function and return a value to the caller. When the generator is called again, it resumes execution from where it was paused, allowing you to generate values one at a time.

Here's an example of a simple generator function that generates a sequence of squared numbers up to a given limit:

def square_generator(limit):
    for i in range(limit):
        yield i ** 2

# Using the generator function
my_generator = square_generator(5)

# Iterating over the generated values
for value in my_generator:
    print(value)


'''Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
first 20 prime numbers.'''

Certainly! Here's an example of a generator function that yields prime numbers less than 1000, and then it uses the `next()` method to print the first 20 prime numbers:

```python
def is_prime(number):
    """Check if a number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def primes_generator():
    """Generator function for prime numbers less than 1000."""
    number = 2
    count = 0
    while count < 20:
        if is_prime(number):
            yield number
            count += 1
        number += 1

# Using the generator function with next() to print the first 20 primes
my_generator = primes_generator()

for _ in range(20):
    print(next(my_generator))


'''Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.'''
a,b=0,1
c=0
print(a)
while(c<10):
    a,b=b,b+a
    c=c+1
    print(a)

'''Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']'''
l='pwskills'
r=[ a for a in l]
print(r)

'''Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.'''
def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number = number // 10

    return original_number == reversed_number

# Input a number from the user
user_number = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(user_number):
    print(f"{user_number} is a palindrome!")
else:
    print(f"{user_number} is not a palindrome.")

'''Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
Note: Use a list comprehension to create a list from 1 to 100 and use another List comprehension to filter
out odd numbers.'''

# List comprehension to create a list from 1 to 100
numbers = [num for num in range(1, 101)]

# List comprehension to filter out odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the list of odd numbers
print(odd_numbers)

