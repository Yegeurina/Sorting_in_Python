import pandas as pd
import cProfile
import psutil

def memory_usage() :
    p=psutil.Process();
    rss = p.memory_info().rss / 2 ** 20 #Byte to MB
    print(f"memory usage : {rss:10.5f}MB")

def quickSort(array) :
  if len(array) <= 1 :
    return array
  p = array[len(array)//2]
  left, pivot, right =[],[],[]
  for num in array :
    if num < p :
      left.append(num)
    elif num > p :
      right.append(num)
    else :
      pivot.append(num)
  return quickSort(left)+pivot+quickSort(right)


if __name__ == '__main__':

    data = pd.Cov = pd.read_csv('./Random.csv')
    random = list(data['0'])
    data = pd.Cov = pd.read_csv('./Sorted.csv')
    sorted = list(data['0'])
    data = pd.Cov = pd.read_csv('./Reversed.csv')
    reversed = list(data['0'])

    memory_usage()
    cProfile.run('quickSort(random)')
    memory_usage()
    cProfile.run('quickSort(sorted)')
    memory_usage()
    cProfile.run('quickSort(reversed)')
    memory_usage()