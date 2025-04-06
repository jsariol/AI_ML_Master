def add_and_substract():
    print("Hello, this is a simple program used to calculate the addition and subtraction of two numbers.\n Please follow the instructions below:")
    try:
        num_1 = int(input('Enter number 1: '))
        num_2 = int(input('Enter number 2: '))
        print(num_1, '+', num_2, '=', num_1 + num_2)
        print(num_1, '-', num_2, '=', num_1 - num_2)
    except ValueError:
        print('Invalid value entered. Please enter a number only.')
add_and_substract()


