"""Write a Python script to print distinct elements along with their frequencies of occurrence in the list."""
l = [1,2,3,4,6,7,8,9,10,2,4,6,8,9,10]
i = 0
for e in l:
    if l.index(e) == i:
        print(e,"-----",l.count(e))
    i+=1
"""""""""""""""""""""""""""""Output"""""""""""""""
"""
1 ----- 1
2 ----- 2
3 ----- 1
4 ----- 2
6 ----- 2
7 ----- 1
8 ----- 2
9 ----- 2
10 ----- 2
"""
