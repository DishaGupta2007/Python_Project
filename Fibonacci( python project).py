import sys
while True:  # Main program loop.
    while True:  # Keep asking until the user enters valid input.
        print('Enter the Nth Fibonacci number ')
        print('calculate (such as 5, 50, 1000, 9999), or QUIT to quit:')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break  # Exit the loop when the user enters a valid number.
        print('Please enter a number greater than 0, or QUIT.')
        print()
    if nth == 1:
        print('0')
        print()
        print('The #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1')
        print()
        print('The #2 Fibonacci number is 1.')
        continue
    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    print('0, 1, ', end='')  # Display the first two Fibonacci numbers.
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1
        print(nextNumber, end='')
        if fibNumbersCalculated == nth:
            print()
            print()
            print('The #', fibNumbersCalculated, ' Fibonacci ',
                  'number is ', nextNumber, '.', sep='')
            break
        print(', ', end='')
        secondToLastNumber = lastNumber
        lastNumber = nextNumber