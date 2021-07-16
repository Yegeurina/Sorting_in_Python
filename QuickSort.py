import pandas as pd
import cProfile
import psutil

def memory_usage() :
    p=psutil.Process();
    rss = p.memory_info().rss / 2 ** 20 #Byte to MB
    print(f"memory usage : {rss:10.5f}MB")

def quickSort(array) :
  if len(array) <= 1 :
      return  array
  p = array[0]
  less, more, pivot = [], [], []
  for num in array :
      if num<p :
          less.append(num)
      elif num>p :
          more.append(num)
      else:
          pivot.append(num)



if __name__ == '__main__':

    data = pd.Cov = pd.read_csv('./Random.csv')
    Random = list(data['0'])
    data = pd.Cov = pd.read_csv('./Sorted.csv')
    Sorted = list(data['0'])
    data = pd.Cov = pd.read_csv('./Reversed.csv')
    Reversed = list(data['0'])

    memory_usage()
    cProfile.run('quickSort(Random)')
    memory_usage()
    cProfile.run('quickSort(Sorted)')
    memory_usage()
    cProfile.run('quickSort(Reversed)')
    memory_usage()
