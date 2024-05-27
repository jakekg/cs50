#strings

#ask the user for their name, remove whitespace from string, & capitaize the first letter of each word
name = input("What's your name?").strip().title()

#print hello & the inputted name
print(f'hello,', {name})


#create our own function

def main():
    
    # output using our own function
    name1 = input("What's your name? ") 
    hello(name1)
    
    #output w/o passing the expected arguments
    hello()

#create our own function
def hello(to='world'):
    print('hello,',to)

main()






