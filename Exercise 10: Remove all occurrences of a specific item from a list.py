# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.

# Given:

# list1 = [5, 20, 15, 20, 25, 50, 20]

# Expected output:

# [5, 15, 25, 50]
def remove_20(list1:list):
    newList:list = [num for num in list1 if num != 20]
    print(newList)
    # while 20 in list1:
    # list1.remove(20)
def main():
    list1 = [5, 20, 15, 20, 25, 50, 20]
    remove_20(list1)
if __name__=="__main__":
    main()