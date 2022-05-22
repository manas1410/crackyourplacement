'''
problem url :- https://www.geeksforgeeks.org/chocolate-distribution-problem/
'''

l = list(map(int,input().split()))
m = int(input())
l.sort()
min_diff = float('inf')
for i in range(0,len(l)):
    try:
        if l[i+m-1]-l[i] < min_diff:
            min_diff = l[i+m-1]-l[i]
    except:
        break
    
print(min_diff)
