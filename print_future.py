#https://www.hackerrank.com/challenges/python-print
#by oz
#print from the future

from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    for num in range(1,n+1):
        print (num, sep='', end='')
