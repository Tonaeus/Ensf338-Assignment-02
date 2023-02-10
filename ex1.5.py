from time import perf_counter
from matplotlib import pyplot as plt

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib2(n, cache={}):
   if n == 0 or n == 1:
       return n
   else:
       if n in cache:
           return cache[n]
       else:
           cache[n] = fib2(n-1)

def main():

    fib1_times = []
    fib2_times = []

    for i in range(0,36):
        start_time = perf_counter()
        fib(i)
        end_time = perf_counter()
        fib1_times.append(end_time - start_time)

    for i in range(0,36):
        start_time = perf_counter()
        fib2(i)
        end_time = perf_counter()
        fib2_times.append(end_time - start_time)

    fig, ax = plt.subplots()

    inputs = [i for i in range(0, 36)]

    ax.plot(inputs, fib1_times)
    ax.plot(inputs, fib2_times)
    plt.show()
    
if __name__ == "__main__":
    main()