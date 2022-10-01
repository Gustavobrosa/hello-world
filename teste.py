"""
a=(1,2,3)
b=[4,5,6]
c={7,8,9}
p,q,r = a
s,t,u = b
x,y,z = c
print(p,q,r)
print(s,t,u)
print(x,y,z)
print(a,b,c)
"""
"""
x=67
y=80
print (x,y)
x,y,z=1,2,3
print(x,y,z)

print ('search'.find('s'))
"""

n = 6
for i in range(0,n,1):
    for j in range(0,i+1):
        print(j,end='')
    print() 
