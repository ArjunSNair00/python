email = input("Enter email: ")
flag = 0

if "@" in email:
    list1 = email.split("@")
    if len(list1) == 2 and list1[0] and list1[1]: #check if repeated @ or empty string 
        if "." in list1[1]:
            list2 = list1[1].split(".")
            if len(list2) >= 2 and all(list2): #ensures no empty domain part uk.com uk.gov.in and not empty gmail. or .com
                tld = list2[-1] #last domain part
                if len(tld) in range(1, 4):
                    print("Valid")
                    flag = 1
if flag == 0:
    print("Invalid")
