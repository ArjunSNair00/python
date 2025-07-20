n=int(input("Enter the number of elements: "))
list=[]
print("Enter the elements of the list: ")
for ia in range(n):
    num=map(int,input().split())
    list.append(num)
print(list)