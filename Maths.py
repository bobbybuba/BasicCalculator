more=input("do you want to do something? Yes/No ")
while more== "Yes":
    
    x = int(input("what is X?"))
    y = int(input("what is Y? "))
   
    Operator = input("what do you want to do? ")

    if Operator == "+": #for addition
        result = (x + y)
    
    elif Operator == "-": #for subtraction
        result = (x - y)
    
    elif Operator == "/": #for division
         result = (x / y)
     
    elif Operator == "*": #for multiplication
         result = (x * y)

    print (result)
    more=input("do you want to do something? Yes/No ")
   
