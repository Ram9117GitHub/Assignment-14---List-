"""Write a Python script to print indices of all occurrences of a given element in a given list."""
l = [eval(x) for x in input("Enter list element :").split(",")]
element = eval (input("Enter element value"))
List = len(l)
for i in range(List):
    if l[i] == element:
        print(i,end=" ")
"""""""""""""""""""""""Output"""""""""""""""
"""
Enter list element :1,3,5,56,6,78,5
Enter element value5
2 6 
"""


