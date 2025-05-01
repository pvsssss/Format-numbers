num = input("enter you number : ")
sep = input("enter the type of seperator you want : ")
# taking the number and the type of seperator as an input from the user


def format(num,sep):
    # creating a function that takes in the number and the seperator and formats it
    
    seperators = ", :';"
    values = "".join(char if char not in seperators else "" for char in num)
    #removes all previous seperators that are already in the number and returns a clean number with only digits

    subvalues = [values[i:i - 3:-1] for i in range( -1 , -len(values)-1, -3)]
    reversed_subvalues = subvalues[::-1]    
    temp = []
    for j in reversed_subvalues:
        temp.append(j[::-1])
    #slices the number into groups of 3
    
    formatted = f"{sep}".join(temp)
    #adds all the substrings together and joins them with the seperator
    
    print(formatted)
    
format(num,sep)
