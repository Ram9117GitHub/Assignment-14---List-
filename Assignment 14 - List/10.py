"""Write a python script to sort a list"""
l = [eval(x) for x in input("Enter list element :").split(",")]
print(l)
l.sort()
print("Sort a List = ",l)
"""""""""""""""""""""""""""""""""Output"""""""""
"""
Enter list element :1,5,7,8,9,5,5,7,7
[1, 5, 7, 8, 9, 5, 5, 7, 7]
Sort a List =  [1, 5, 5, 5, 7, 7, 7, 8, 9]
"""