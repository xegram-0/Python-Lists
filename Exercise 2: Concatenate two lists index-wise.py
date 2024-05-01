# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given:

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# Expected output:

# ['My', 'name', 'is', 'Kelly']
def concatenate_lists(list1:list, list2:list):
    finalList:list = [word1+word2 for word1,word2 in zip(list1,list2)]
    #finalList:list = zip(list1,list2)
    print(finalList)
def main():
    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    concatenate_lists(list1,list2)
if __name__=="__main__":
    main()
