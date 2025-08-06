list_1=[1,7,9,4,6,2]
target=6
for i in range(len(list_1)):
    if target==list_1[i]:
        print(i)
        break

#################################

list_1=[1,2,3,4,5,6,7,8,9,10]
target=9
start=0
end=len(list_1)-1
index=-1
while(start<=end):
    middle=(start+end)//2
    if list_1[middle]==target:
        index=(middle)
        break
    elif list_1[middle]>target:
        end=middle-1
    elif list_1[middle]<target:
        start=middle+1
    print(index)
    
####################################

