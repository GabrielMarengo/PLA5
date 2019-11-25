import random as rand
import itertools

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


def parallelIter(l1 = [1,2], l2 = [3,4]):
    return [x for x in itertools.chain(*itertools.zip_longest(l1, l2)) if x is not None]

# TODO: Make
def all_iter(l1 =[1,2], l2 = [3,4]):
    pass
    # l3 = itertools.chain(l1, l2)
    # myList = [x for x in itertools.permutations(l3, 4) if x is not None]
    # for x in list(myList):
    #     if 0 in x:
    #         print(x)
    #         myList.remove(x)
    # return myList



def problem4():
    # 1 = on
    # 0 = off
    lightsOut = [[0]*5, [0]*5, [0]*5, [0]*5, [0]*5]
    # randomizes the input
    for row in lightsOut:
        for pos in range(5):
            row[pos] = rand.randrange(2)

    for row in lightsOut:
        print(row)

    def change(number):
        if number == 1:
            number = 0
        else:
            number = 1

        return number

    def click(row, pos):
        lightsOut[row][pos] = change(lightsOut[row][pos])
        if not row == 0:
            lightsOut[row-1][pos] = change(lightsOut[row-1][pos])
        if not row == 4:
            lightsOut[row+1][pos] = change(lightsOut[row+1][pos])

        if not pos == 0:
            lightsOut[row][pos-1] = change(lightsOut[row][pos-1])

        if not pos == 4:
            lightsOut[row][pos+1] = change(lightsOut[row][pos+1])

    def light_chase():
        for row in range(4):
            for pos in range(5):
                if lightsOut[row][pos] == 1:
                    click(row+1, pos)

    def change_first_row():
        if lightsOut[4] == [0,0,1,1,1]:
            click(0,3)
        elif lightsOut[4] == [0,1,0,1,0]:
            click(0,1)
            click(0,4)
        elif lightsOut[4] == [0,1,1,0,1]:
            click(0,0)
        elif lightsOut[4] == [1,0,0,0,1]:
            click(0,3)
            click(0,4)
        elif lightsOut[4] == [1,0,1,1,0]:
            click(0,4)
        elif lightsOut[4] == [1,1,0,1,1]:
            click(0,2)
        elif lightsOut[4] == [1,1,1,0,0]:
            click(0,1)

    change_first_row()
    light_chase()
    if not lightsOut[4] == [0,0,0,0,0]:
        change_first_row()
        light_chase()


    if lightsOut[4] == [0,0,0,0,0]:
        msg = "It has been solved:"
    else:
        msg = "No solution available:"
    print("\n" + msg)
    for row in lightsOut:
        print(row)





def main():
    # Problem 1
    print("Problem 1")
    problem1()

    # Problem 2
    print("\nProblem 2")
    problem2()

    # Problem 3
    print("\nProblem 3:")
    print(parallelIter())
    print(all_iter())

    # Problem 4
    print("\nProblem 4")
    problem4()


if __name__ == "__main__":
    main()

# Problem 4 solution method: http://www.logicgamesonline.com/lightsout/tutorial.html