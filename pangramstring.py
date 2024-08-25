def pangram (input_string):
    
    input_string = input_string.lower()
    create_set = set()
    
    for i in input_string:
        if 'a' <= i <= 'z':
            create_set.add(i)

    if len(create_set) == 26:
        return True 
    else:
        return False

input_string = input ('Enter the string: ')
if pangram (input_string) == True:
    print("It's a pangram! ")
else:
    print("It's not a pangram.")