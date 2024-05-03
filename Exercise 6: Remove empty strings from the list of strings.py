# Exercise 6: Remove empty strings from the list of strings
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Expected output:

# ["Mike", "Emma", "Kelly", "Brad"]
import re

def filter_blank(name):
    if name == "":
        return None
    else:
        return True
def main():
    list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
    # newList = re.sub(r"\s","_",list1)
    # Cannot use re.sub since this is a list
    # not a string
    newList:list = list(filter(filter_blank,list1))
    #res = list(filter(None, list1))
    print(newList)
if __name__=="__main__":
    main()