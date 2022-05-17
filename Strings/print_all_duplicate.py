'''
Problem url - https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/
'''
'''
Approach - 
Using dictionary store each characters count and then print which has count more than 1.
'''
s = input()
d = {}
for i in s:
    try:
        d[i] +=1 
    except:
        d[i] = 1 
for i in d.keys():
    if d[i]>1:
        print("{}, count = {}".format(i,d[i]))
