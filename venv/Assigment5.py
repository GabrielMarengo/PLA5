
def addPositiveInts(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum


def problem1():
    errors = 0
    while True:
        try:
            num1 = int(input("Enter a positive integer up to 123456789: "))
        except ValueError:
            if errors < 3:
                errors += 1
                print("The input provided was not an integer")
                continue
            else:
                print("Incorrect input exceeds 3 times")
                break

        if (num1 < 0) or (num1 > 123456789):
            if errors < 3:
                errors += 1
                print("The input provided is negative or greater than 123456789")
                continue
            else:
                print("Incorrect input exceeds 3 times")
                break

        else:
            print(str(addPositiveInts(num1)))
            return


def secondPrimeNum(a):
    second = False
    for i in range(a, 5001):

        # isPrime variable to tell if i is prime or not
        isPrime = True

        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                isPrime = False
                break

        if (isPrime):
            if(second):
                print(i, end=" ")
                return
            second = True

    print("No second prime number can be found after {} that is smaller than 5000".format(a))

def problem2():
    errors = 0
    while True:
        try:
            num2 = int(input("Enter a positive integer between 1000 and 5000: "))
        except ValueError:
            if errors < 3:
                errors += 1
                print("The input provided was not an integer")
                continue
            else:
                print("Incorrect input exceeds 3 times")
                break

        if (num2 < 1000) or (num2 >= 5000):
            if errors < 3:
                errors += 1
                print("The input provided is smaller than 1000 or greater or equal to 5000")
                continue
            else:
                print("Incorrect input exceeds 3 times")
                break

        else:
            secondPrimeNum(num2)
            break


def parallelIter():
    def twolists(l1, l2):
        return [x for x in chain.from_iterable(zip_longest(l1, l2)) if x is not None]


def main():
    # Problem 1
    print("Problem 1")
    problem1()

    # Problem 2
    print("\nProblem 2")
    problem2()


if __name__ == "__main__":
    main()