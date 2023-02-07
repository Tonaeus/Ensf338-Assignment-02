import matplotlib.pyplot as plt
from time import perf_counter
import sys
import json
from urllib.request import urlopen
import timeit



sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
        
def func2(array, start, end):
    ## start new code
    p = median(array,start,end, (start + end) // 2)
    array[start], array[p] = array[p], array[start]
    p = list[start]
    ## end new code
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

## start new code
def median(a, i, j, k):
  if a[i] < a[j]:
    return i if a[k] < a[i] else k if a[k] < a[j] else j
  else:
    return j if a[k] < a[j] else k if a[k] < a[i] else i
## end new code

url = "https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json"
response = urlopen(url)
data_json = json.loads(response.read())
  
resultTime = []
resultLength = []

for list in data_json:
    time = timeit.timeit(lambda:func1(list,50,len(list)-1), number=100)
    resultLength.append(len(list))
    resultTime.append(time)

plt.plot(resultLength,resultTime)
plt.show()

