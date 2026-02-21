print("-"*45)
wel = ("Welcome to the char type identifier program \nEnter 'quit' for exit")
print(wel)
print("-"*45)

def char_type():
    char = input("\nEnter your char: ").strip()

    if char.lower() == 'quit':
        return False


    if len(char)==1:
    
        if char.isupper():
            print(f"Result: Enter {char} is 'UPPERCASE")

        elif char.islower():
            print(f"Result: Enter {char} is 'lowercase")

        elif char.isdigit():
            print(f"Result: entre {char} is 'Number")

        else:
            print(f"Result:enter {char} is 'Speical char")

    else:
        print(f"Result: Invalid {char}! Please enter single char")


count = 0
while count < 5:
    status = char_type()
    if status == False:
            break
    count +=1

print("Program Closed , Have a great day..!")





      

        
