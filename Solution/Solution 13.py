n=int(input("Enter num of rows:"))
i=0
j=0

for i in range(i,n):
    for j in range(0,i+1):
        print(end="  ")
    for j in range(i,n):
        print("*",end="")
    
    print("\r")
