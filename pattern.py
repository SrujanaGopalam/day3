''''#triangle * pattern
n=int(input("enter number: "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end ="  ")
    print()

#triangle * pattern
n=int(input())
for i in range(1,n+1):
    print("*  "*i)

#inverted *pattern
n=int(input())
for i in range(n,0,-1):
    print("*  "*i)

#triangle number pattern
n=int(input("Enter:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="  ")
    print()

#triangle number pattern 2
n=int(input("Enter:"))
for i in range(1,n+1):
    str1=""
    for j in range(1,i+1):
        str1=str1+str(j)+"  "
    print(str1)

#inverted number patter
n=int(input("Enter:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="  ")
    print()

#inverted method2
n=int(input("Enter:"))
for i in range(n,0,-1):
    str1=""
    for j in range(1,i+1):
        str1=str1+str(j)+"   "
    print(str1)

#pyramid pattern
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)

#inverted pyramid
n=int(input("Enter:"))
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)

#number pyramid
n=int(input("Enter:"))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
    
#hallow triangle
n=int(input("Enter:"))
for i in range(1,n+1):
    if i==1 or i==n:
        print("* "*i)
    else:
        print("*"+" "*(2*i-3)+"*" )''''

#hallow pyramid
n=int(input("Enter:"))
for i in range(1,n+1):
    if i==1 or i==n:n 
        print()