# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

# Given:

# list1 = [5, 10, 15, 20, 25, 50, 20]

# Expected output:

# [5, 10, 15, 200, 25, 50, 20]

def replace_value(list1:list):
    posNum:int = list1.index(20)
    list1[posNum] = 200
    print(list1)
def main():
    list1 = [5, 10, 15, 20, 25, 50, 20]
    replace_value(list1)
if __name__=="__main__":
    main()