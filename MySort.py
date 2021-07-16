import pandas as pd
import cProfile
import psutil

def memory_usage() :
    p=psutil.Process();
    rss = p.memory_info().rss / 2 ** 20 #Byte to MB
    print(f"memory usage : {rss:10.5f}MB")

def mySort(array) :
    if len(array) <= 1:
        return array
    p = array[len(array) // 2]
    left, pivot, right = [], [], []
    for num in array:
        if num < p:
            left.append(num)
        elif num > p:
            right.append(num)
        else:
            pivot.append(num)
    return mySort(left) + pivot + mySort(right)


if __name__ == '__main__':

    data = pd.Cov = pd.read_csv('./Random.csv')
    Random = list(data['0'])
    data = pd.Cov = pd.read_csv('./Sorted.csv')
    Sorted = list(data['0'])
    data = pd.Cov = pd.read_csv('./Reversed.csv')
    Reversed = list(data['0'])

    memory_usage()
    cProfile.run('mySort(Random)')
    memory_usage()
    cProfile.run('mySort(Sorted)')
    memory_usage()
    cProfile.run('mySort(Reversed)')
    memory_usage()