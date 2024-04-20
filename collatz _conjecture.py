# Collatz Conjecture
 
def collatz_sequence():
    n = input("Enter a number greater than 1.\n")
    try:
        n = int(n)
        if n <= 1:
            print('Number is not greater than 1.')
        else:
            steps = 0
            while n != 1:
                if (n % 2) == 0:
                    n = n // 2
                    print(n)
                    steps += 1
                else:
                    n = n * 3 + 1
                    print(n)
                    steps += 1
                if n == 1:
                    print(f"The number of steps in the Collatz Sequence is {steps}.")
                    break
    except ValueError:
        print('Input is not an integer.')

collatz_sequence()