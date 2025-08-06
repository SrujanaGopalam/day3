n=int(input("enter number: "))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end ="  ")
    print()

#############################

n=int(input())
for i in range(1,n+1):
    print("*  "*i)

####################################

n=int(input())
for i in range(n,0,-1):
    print("*  "*i)

####################################

n=int(input("Enter:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="  ")
    print()

######################################

n=int(input("Enter:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="  ")
    print()