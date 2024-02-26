"""
Fibonacci Series
@autor lufemoal19
@since 02/25/2025
"""

# Fibonacci series as list
def fibonacci_iterator_series(number):
    # Taking 1st two fibonacci numbers as 0 and 1
    sequence = [0, 1]

    for item in range(2, number + 1):
        sequence.append(sequence[item - 1] + sequence[item - 2])
    
    return sequence

# Fibonacci series using Dynamic Programming
def fibonacci_iterator(number):
    # Taking 1st two fibonacci numbers as 0 and 1
    sequence = [0, 1]

    for item in range(2, number + 1):
        sequence.append(sequence[item - 1] + sequence[item - 2])
    
    return sequence[number]

# Fibonacci series using recursion
def fibonacci_recursion(number):
    if number <= 1:
        return number
    return fibonacci_recursion(number - 1) + fibonacci_recursion(number - 2)

def main():
    
    number = 14

    print(f'Number = {number}\nFib iterator: {fibonacci_iterator(number)}\nFib recursion: {fibonacci_recursion(number)}\nFib series {fibonacci_iterator_series(number)}')

    pass

if __name__ == '__main__':
    main()