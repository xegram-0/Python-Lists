# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.

# Given

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# Expected output:

# 10 400
# 20 300
# 30 200
# 40 100
def iterate_both_list(list1:list,list2:list):
    reversedList2:list = list(reversed(list2))
    listTuple:tuple = list((zip(list1,reversedList2)))
    for _ in listTuple:
        print(_)

    # for x, y in zip(list1, list2[::-1]):
    # print(x, y)
def main():
    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    iterate_both_list(list1,list2)
if __name__=="__main__":
    main()