#!/usr/local/bin/python3
'''
Program to find square root of a number
using Newton-Raphson method.
'''

if __name__ == '__main__':
  num = int(input("Enter a positive value:"))
  if num > 0:
    epsilon = 0.00001
    guess = num / 2
    while abs(guess ** 2 - num) > epsilon:
      print(guess)
      guess = guess - ((guess ** 2 - num) / (2 * guess))
    print("Approximate square root of {} is {}".format(num, guess))
  else:
    print("Cannot find square root of a negative number")
