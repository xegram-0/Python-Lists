# Exercise 1: Reverse a list in Python

# Given:

# list1 = [100, 200, 300, 400, 500]

# Expected output:

# [500, 400, 300, 200, 100]

def main():
    list1 = [100, 200, 300, 400, 500]
    reversedList:list = list(reversed(list1))
    print(reversedList)
    # Odd way this method operates
    #list1.reverse()
    #print(list1)
if __name__=="__main__":
    main()