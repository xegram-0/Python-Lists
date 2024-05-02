# Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]

# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
def concatenate_lists(list1:list,list2:list):
    concatenatedList:list = []
    #concatenatedList:list = [x + y for x in list1 for y in list2]
    for word1 in list1:
        for word2 in list2:
            concatenatedList.append(word1+word2)
    print(concatenatedList)

def main():
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    concatenate_lists(list1,list2)
if __name__=="__main__":
    main()