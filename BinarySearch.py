a = []
n = int(input("ENter limit of array :"))
for i in range(0,n):
    ele = int(input("Enter element in array :"))
    a.append(ele)
    
search = int(input("\nEnter a number to find :"))
    
low = 0
high = n - 1
flag = 0

while(low <= high):
    middle = (low+high) // 2
    if(a[middle] < search):
        low = middle + 1
    elif(a[middle] == search):
        print(f"{search} found at location {middle+1}\n")
        flag = 1
        break
    else:
        high = middle - 1
if(flag == 0):
    print(f"{search} not found in array")