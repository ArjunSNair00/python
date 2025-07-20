n=int(input("Enter number of tuples: "))
list=[]
for i in range(n):
  m=int(input("Enter the number of elements in the tuple "+str(i+1)+":"))
  list1=[]
  for j in range(m):
    x=int(input(f"Enter element {j+1}:"))
    list1.append(x)
  tuple1=tuple(list1)
  list.append(tuple1)
print("The list is : ",list)
even=[]
odd=[]
mixed=[]

for i in range(n):
  tuple2=list[i]
  flage=0
  flago=0
  for j in tuple2:
    if j%2==0:
      flage=1
    else:
      flago=1
  if flage==1 and flago==0:
    even.append(tuple2)
  if flage==0 and flago==1:
    odd.append(tuple2)
  if flage==1 and flago==1:
    mixed.append(tuple2)
print("The even list is : ",even)
print("The odd list is : ",odd)
print("The mixed list is : ",mixed)