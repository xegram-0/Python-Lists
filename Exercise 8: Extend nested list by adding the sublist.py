# Exercise 8: Extend nested list by adding the sublist
# You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.

# Given List:

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# # sub list to add
# sub_list = ["h", "i", "j"]

# Expected Output:

# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

def add_subList(list1:list,sub_list:list):
    list1[2][1][2].extend(sub_list)
    # extend to remvoe the list
    # and add the elements directly into the list
    # kinda like append but more stuff instead of one
    print(list1)

def main():
    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    sub_list = ["h", "i", "j"]

    add_subList(list1,sub_list)
if __name__=="__main__":
    main()