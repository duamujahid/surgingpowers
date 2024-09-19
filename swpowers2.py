def powerof4(Number):
    # number= int(input("Enter your Number : "))
    count = 0

    if (number & (~(number & (number - 1)))):
       while(number > 1):
        number >>= 1
        count += 1

    if(count % 2 == 0):
        return True
    else:
        return False



x = int(input("Enter the number you want to check : "))
print(powerof4(x))


def printName(name, grade , schoolName):
    print(name)
    print(grade)
    print(schoolName)
    
    
    
    


n = input("enter your name")
g = input("Enter your grade : ")
schoolName = input("Enter your grade : ")

printName(n , g , schoolName)