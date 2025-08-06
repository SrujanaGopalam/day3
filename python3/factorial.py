n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
print("the factorial of",n, "is",fact)

################

n=int(input())
s=0
for i in range(1,11):
    s+=n*i
print("the sum of 10 multiples of",n,"is",s)
