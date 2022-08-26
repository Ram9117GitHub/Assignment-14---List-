"""Write a Python script to remove all non int values from a list"""
l = [1,'non',2.3,"non",2]
rem = []
for x in l:
    if str(x) != 'non':
        rem.append(x)
print(rem)
"""""""""""""""""""""""""""Output"""""
"""
[1, 2.3, 2]
"""
