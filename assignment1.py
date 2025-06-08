#UPPER TRIANGULAR
def upper_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)
#for example
upper_triangle(5)


# LOWER TRIANGULAR
rows = 5
for i in range(rows, 0, -1):
    print("* " * i)



# Pyramid
def pyramid(n):
    print("Pyramid Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)
    print()
# Example usage
pyramid(5)

