def divide_and_multiply():
    print("Hello, this is a simple program used to calculate the multiplication and division of two numbers.\n\n Please follow the instructions below:")
    try:        
        num_1 = int(input('Enter number 1: '))
        num_2 = int(input('Enter number 2: '))
        if num_2 == 0:
            print('Invalid value entered. For second number, please enter any number except zero.')
        else:
            print(num_1, '*', num_2, '=', num_1 * num_2)
            print(num_1, '/', num_2, '=', num_1 / num_2)    
    except ValueError:
        print('Invalid value entered. Please enter a number only.')       
divide_and_multiply()


