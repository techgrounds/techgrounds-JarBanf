# list of 5 integers
integers = [3, 6, 23, 43, 50]

# loop through the list items by their index number
# from [0] - [last index]
for i in range(len(integers)):
    # if index number is NOT the last, 
    # current index value + next index value
    if i != (len(integers) - 1):
        print(integers[i]+integers[i+1])
    # else we have reached the last index
    # in this case, add last index value + first index value
    else:
        print(integers[i]+integers[i-i])