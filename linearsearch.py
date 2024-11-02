arr = []
n = int(input("Enter the limit :"))
for i in range(0,n):
    ele = int(input("ENter Element in array :"))
    arr.append(ele)
    
print(arr)

flag = 0
#cnt = 0
search = int(input("Enter ele to search :"))
for i in range(0,len(arr)):
    if(arr[i] == search):
        #cnt += 1
        print(f"Element {search} found on index {i}.\n")
        flag = 1
        break
    
if(flag == 0):
    print("Element not found...!")
# else:
#     print(f"Element {search} found and {cnt} times.")