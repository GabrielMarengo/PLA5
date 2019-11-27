import random as rand
import itertools


def problem1(num = 123456789):
    def addPositiveInts(num=123456789):
        return sum(range(num + 1))
    print("Sum of {} is: {}".format(num, addPositiveInts(num)))




def problem2(num = 1000):
    def secondPrimeNum(a=1000):
        second = False
        for i in range(a, 5001):

            # isPrime variable to tell if i is prime or not
            isPrime = True

            for j in range(2, i // 2 + 1):
                if (i % j == 0):
                    isPrime = False
                    break

            if (isPrime):
                if (second):
                    return i
                second = True
    print("The second prime number for {} is: {}".format(num, secondPrimeNum(num)))



def problem3(l1 = [1, 2], l2 = [3, 4]):
    def parallel_iter(l1=[1, 2], l2=[3, 4]):
        return [x for x in itertools.chain(*itertools.zip_longest(l1, l2)) if x is not None]

    def all_iter(l1=[1, 2], l2=[3, 4]):
        all_iter_list = []

        def all_iter_recursive(l1, l2, lengthL1=len(l1), lengthL2=len(l2), iStr=[''] * (len(l1) + len(l2)), i=0):
            # Base case: If all numbers of l1 and l2 have been included in the interleaved string,
            # then adds it to the interleaved list
            if lengthL1 == 0 and lengthL2 == 0:
                all_iter_list.append(list(map(int, iStr)))

            if lengthL1 != 0:
                iStr[i] = l1[0]
                all_iter_recursive(l1[1:], l2, lengthL1 - 1, lengthL2, iStr, i + 1)

            if lengthL2 != 0:
                iStr[i] = l2[0]
                all_iter_recursive(l1, l2[1:], lengthL1, lengthL2 - 1, iStr, i + 1)

        l1 = "".join(map(str, l1))
        l2 = "".join(map(str, l2))
        all_iter_recursive(l1, l2)
        return all_iter_list

    print(parallel_iter(l1,l2))
    print("\nAll-iter:")
    print(*all_iter(l1,l2), sep="\n")

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
    print("Problem 1:")
    problem1()

    # Problem 2
    print("\n\nProblem 2:")
    problem2()

    # Problem 3
    print("\n\nProblem 3:\nParallel-iter:")
    problem3()

    # Problem 4
    print("\n\nProblem 4")
    problem4()


if __name__ == "__main__":
    main()

# Problem 4 solution method: http://www.logicgamesonline.com/lightsout/tutorial.html