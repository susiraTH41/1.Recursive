def ads(num):
    if num <= 0:
        return
    elif num%3 == 0:
        lit3.append(num)
        
    elif num%5 == 0:
        lit5.append(num)
        
    elif num%7 == 0:
        lit7.append(num)
        
    return ads(num-1)

lit3=[]
lit5=[]
lit7=[]   
num = int(input("Input : "))
ads(num)

print("Output")
print("group#3  "+str(lit3[::-1]))
print("group#5  "+str(lit5[::-1]))
print("group#7  "+str(lit7[::-1]))
