email=input("Enter email : ")
flag=0
for i in range(len(email)):
    if email[i]=="@":
        list1=email.split("@")
        list2=list1[1].split(".")
        length=len(list2[1])
        if length in range(1,4):
            print("Valid")
            flag=1
            break
if flag==0:
    print("Invalid")