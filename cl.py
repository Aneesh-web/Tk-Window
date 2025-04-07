# Function to calculate Fibonacci number using recursion and pow
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return pow(fibonacci(n - 1), 1) + pow(fibonacci(n - 2), 1)

# Function to calculate the sum of the first n Fibonacci numbers
def sum_of_numbers(n):
    total_sum = 0
    for i in range(n):
        total_sum += fibonacci(i)
    return total_sum

# Test the functions
terms = 10  # Number of Fibonacci terms to generate

# Print the Fibonacci sequence
print("Fibonacci sequence:")
for i in range(terms):
    print(fibonacci(i), end=" ")

# Print the sum of Fibonacci numbers
total_sum = sum_of_numbers(terms)
print(f"\n\nSum of the first {terms} Fibonacci numbers: {total_sum}")
