n=int(input("Enter a number of elements: "))
list_l=[]
print("Enter the elements: ")
for i in range(n):
    number=int(input())
    list_l.append(number)
print("Entered list contains: \n",list_l)
num=int(input("Enter number whose occurence to be removed: "))