#this function takes in 2 number and returns the calculated average of these 2 numbers
def avg(num1, num2):
    return (num1+num2)/2
    
x = 128
y = 255
z = avg(x,y) #stores the return value of the avg() function in variable z

print("The average of",x,"and",y,"is",z)