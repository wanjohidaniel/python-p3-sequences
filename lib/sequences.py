#!/usr/bin/env python3

def print_fibonacci(n):
    if n < 1:
        print([])
        return
    
    fibonacci_sequence = [0]
    
    if n > 1:
        fibonacci_sequence.append(1)
    
    while len(fibonacci_sequence) < n:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    
    print(fibonacci_sequence)

