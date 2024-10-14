rows = int(input("Please enter how many rows you need: "))  
num = rows  
for i in range(rows, 0, -1):  
    for j in range(0, i):  
        print(num, end=' ')  
    print () #for printing a new line  
