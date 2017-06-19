"""
Python code to print nultiple Fibo values
input: STDIN input
Num1
Num2
Num3

output:
print Fibo NumX value

"""

import sys

x=sys.stdin.readlines()
m = [int(i) for i in x]
n = m
#n.sort()
result = {}


if(max(n)<3):
    if(0 in n):
        result.update({0:0})
    if(1 in n):
        result.update({1:1})
    if(2 in n):
        result.update({2:1})
else:
    
    if(0 in n):
        result.update({0:0})
    if(1 in n):
        result.update({1:1})
    if(2 in n):
        result.update({2:1})
    i=2
    k=max(n)
    prev = 1
    current = 1
    while(i<=k):
        i+=1
        
        fib = current+prev
        prev = current
        current = fib
        if(i in n):
            result.update({i:fib})
#print(m)
for i in m:
    print(result[i])
        
            
                












