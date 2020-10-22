# importing required modules
from math import pi
from math import e as ex
import random
import operator


# equation for getting the value of function Y at given value of x
# parameters = mean, standard deviation, x
# return     = value of Y at x
from typing import TextIO


def NORMDIST(x, mean, sd):
    part1 = 1 / (sd * ((2 * pi) ** (1 / 2)))
    part2 = ex ** (-((x - mean) ** 2) / (2 * (sd ** 2)))

    y = part1 * part2
    return y


# Getting the required graph from user
# and converting it into adjacentary matrix

##############  NOTE  ###############
# For each note user has to enter the connected nodes with it

def GetGraph(N):
    graph = []

    for i in range(N):
        templs = [int(x) for x in input(f'Enter adjacent nodes of {i + 1}st NODE: ').split()]
        temp = []
        for i in range(N):
            temp.append(0)
        for i in templs:
            temp[i - 1] = 1
        graph.append(temp)

    return graph


# This function initiates and make required variables(storage) for the
def init(N, mean, stddev, min, max):
    output = []  # for storing the guessed value
    temp1 = []  # for storing the temporary value
    temp2 = []  # for storing the temporary value
    lastval = []
    # for each Node it is storing four values in 2 differnet
    # temporary storage which will be used interchangebly
    for i in range(N):
        temp = []  # creating temp list for the loop
        output.append([])  # add empty list for output
        temp.append(min)  # adding min value at temp[0] i.e -4
        temp.append(max)  # adding max value at temp[1] i.e 4
        temp.append(round(random.uniform(min, max), 1))  # adding random value at temp[2]
        temp.append(NORMDIST(temp[2], mean, stddev))  # adding value of Y at gussed value of X
        temp1.append(temp)  # adding the temp to temporary storage temp1
        temp2.append(temp)  # adding the temp to temporary storage temp2
        lastval.append(
            0)  # it will be used for exiting the RECURSION Later, also it store last-guessed values of each Node
        # at starign it stores 0's
        output[i].append(temp[2])

    return output, lastval, temp1, temp2


def solveit(graph, temp, row, mean, stddev):
    N = len(graph)  # calculated numbers of nodes
    minlist = [abs(abs(mean - temp[row][0]) - 0.1), abs(abs(mean - temp[row][1]) - 0.1),
               abs(abs(mean - temp[row][2]) - 0.1)]  # make a temporary list for storing all the guessed values

    # Now storing the Guessed VALUES by the same node
    for i in range(N):
        if graph[i] == 1:
            # Now storing the Guessed VALUES of the connected Nodes
            minlist.append(abs(abs(mean - temp[i][2]) - 0.1))
            minlist.append(abs(abs(mean - temp[i][2]) - 0.1))
    # Sorting the temporary list
    minlist.sort()
    max =mean+ minlist[0]  # Getting the smallest possible value for sorting the range
    min =mean- minlist[0] # Sorting the guessing range and storign value in min and max
    res = [min, max,
           round(random.uniform(min, max), 1)]  # creating a list for returning min, max, guessed value , and value of Y
    res.append(NORMDIST(res[2], mean, stddev))
    return res


# combining all The  stuff here
def runcode():
    mean = float(input("Please enter mean                         "))
    stddev = float(input("Please enter standard deviation           "))
    min, max = [float(x) for x in input("Please enter Range for X i.e [min , max]  ").split()]
    N = int(input("Enter no. of Nodes                       "))  # getting no of nodes
    graph = GetGraph(N)                                          # Getting graph in adjacentry matrix form
    # Initializing the matrix and getting other required storage for calculation
    output, lastval, temp1, temp2 = init(N, mean, stddev, min, max)
    flag = 1

    def compute(graph, output, lastval, temp1, temp2, flag, mean, stddev):
        temp = []  # making a temporary list for return values
        maxValues = []  # Local variable for storing maxValues in the list
        N = len(graph)  # calculating nodes of graph
        if flag == 1:
            for i in range(N):
                res = solveit(graph[i], temp1, i, mean, stddev)  # calling function
                temp.append(res[3])  # adding returend value of y to temporary list
                output[i].append(res[2])
                temp2[i] = res
            flag = 2
        else:
            for i in range(N):
                res = solveit(graph[i], temp2, i, mean, stddev)  # calling function
                temp.append(res[3])  # adding returend value of y to temporary list
                output[i].append(res[2])
                temp1[i] = res
            flag = 1

        check = False
        # checking the maxima is reached by checking whether last value is greater/equal (>=) than current value
        for i in range(N):
            if lastval[i] >= temp[i]: # if yes, then
                maxValues.append([lastval[i], output[i][-2], i + 1])    # store those value in temporary list
                check = True          # change check = True for exiting the recursion
            else:                      # otherwise
                lastval[i] = temp[i]    # update the last values

        if check:                      # Checking whether check == True for exiting
            # sorting maxValues list in descending order
            maxValuesSort = sorted(maxValues, key=operator.itemgetter(0), reverse=True)
            # printing the Maxima(maximum value, at x, by node)
            print("\n")
            for i in range(len(maxValuesSort)):
                print(
                    f'MaxValue = {maxValuesSort[i][0]} at {maxValuesSort[i][1]} guessed By Node : {maxValuesSort[i][2]}')
            return
        else:
            # else call the recursive function again
            compute(graph, output, lastval, temp1, temp2, flag, mean, stddev)
    # start the recursive function
    compute(graph, output, lastval, temp1, temp2, flag, mean, stddev)

    # Store the Guessed values of each node to the file named guessValues.txt
    print('\n\n -------------------OUTPUT for file------------------- ')
    for i in range(N):
        print(f'Guess of {i + 1} = {output[i][:-1]}')
    guessfile: TextIO = open('guesses.txt', 'a')
    guessfile.writelines('\n--------------------------------------------------\n')
    for i in range(N):
        temp = f'Guess of {i + 1} = {output[i][:-1]}\n'
        guessfile.writelines(temp)

    guessfile.close()

runcode()
