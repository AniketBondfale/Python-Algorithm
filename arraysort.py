arr = []
n = int(input("Enter the limit :"))
for i in range(0,n):
    ele = int(input("ENter Element in array :"))
    arr.append(ele)
    
print(arr)

temp = 0
for i in range(0,len(arr)):
    for j in range(0,n - i - 1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)