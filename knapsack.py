#!/usr/on

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])
CostItem = namedtuple('CostItem',['index','costValue'])

file_contents = open('data/small1.txt', 'r')

def knapsack_solver(items, capacity, n, value):
    if capacity == 0 or n == 0:
        return 0

    if (items.[n-1] > capacity):
        return knapsack_solver(items, capacity,  n-1, value)

    else:
        return max(value[n-1] + knapsack_solver(items,capacity - items[1][n - 1], n-1), knapsack_solver(items, capacity, n - 1, value))
if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')


    knapsack_solver(file_contents, 100)
