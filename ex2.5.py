import matplotlib.pyplot as plt
from time import perf_counter
import sys
import json
from urllib.request import urlopen
import timeit
import random

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

def read_file(filename):
    """
    A function that reads a json file

    Parameters: filename
    Return: file's content

    """
    with open(filename, "r") as infile:
        return json.load(infile)

def main():
    data_json = read_file("ex2.5.json")
    
    resultTime = []
    resultLength = []
    for list in data_json:
        time = timeit.timeit(lambda:func1(list,0,len(list)-1), number=1)
        resultLength.append(len(list))
        resultTime.append(time)

    plt.plot(resultLength,resultTime)
    plt.show()
    print(resultTime)
    
if __name__ == "__main__":
    main()