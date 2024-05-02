# Exercise 3: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.

# Given:

# numbers = [1, 2, 3, 4, 5, 6, 7]

# Expected output:

# [1, 4, 9, 16, 25, 36, 49]
def square_number(numbers:list):
    squareList:list = [number**2 for number in numbers]
    print(squareList)
def main():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    square_number(numbers)
if __name__=="__main__":
    main()