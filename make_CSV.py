from bigO import BigO
import csv
import pandas as pd

def generater():
    lib = BigO()
    size = 100000

    #Random
    randomNum=lib.genRandomArray(size)
    data1=pd.DataFrame(randomNum)
    data1.to_csv('./Random.csv')

    #Sorted
    sortedNum = lib.genSortedArray(size)
    data2=pd.DataFrame(sortedNum)
    data2.to_csv('./Sorted.csv')

    #Reversed
    reversedNum=lib.genReversedArray(size)
    data3 = pd.DataFrame(reversedNum)
    data3.to_csv('./Reversed.csv')

if __name__ == '__main__':
    generater()

