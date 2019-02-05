import re

print('Basic Calculator')
print("Type 'quit' to exit")
print("Type 'reopen' to start with 0\n")
print("Type 'help' if you need")

previous = 0
run = True


def perform_math():
    global run
    global previous
    equation = ''
    
    if previous == 0:
        equation = input('Enter equation: ')
        
    else:
        equation = input(str(previous) + ' ')
        
    if equation == 'quit':
        run = False
        print('Goodbye Human!')        
        
    elif equation == "help":
        print('This terminal calculator is degined for generel purpose')
        
    elif equation == 'reopen':
        previous = 0

    else:
        equation = re.sub('[a-zA-Z,:.()@#!$^&_=;\'|><" "]', '', equation)
        
        if previous == 0:
            previous = eval(equation)
            
        else:
            previous = eval(str(previous) + equation)

while run:
    perform_math()
