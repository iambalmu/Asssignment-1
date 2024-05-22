def lower_triangular(n):
    print("Lower Triangular Pattern:")
    for i in range(1, n + 1):
        print('* ' * i)
    print()  # Adding a new line for better readability

def upper_triangular(n):
    print("Upper Triangular Pattern:")
    for i in range(n, 0, -1):
        print('* ' * i)
    print()  # Adding a new line for better readability

def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(n):
        # Print leading spaces
        print(' ' * (n - i - 1), end='')
        # Print stars
        print('* ' * (i + 1))
    print()  # Adding a new line for better readability

# Example usage:
n = 5
lower_triangular(n)
upper_triangular(n)
pyramid(n)
