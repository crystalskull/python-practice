#!/usr/local/bin/python3
'''
Program to find square root of a number using bisection
search method.
'''
if __name__ == '__main__':
  num = int(input("Enter a positive number:"))
  if num > 0:
    epsilon = 0.00001
    low = 0
    high = max(1, num)
    guess = (low + high) / 2
    while abs(guess ** 2 - num) > epsilon:
      print(low, high, guess)
      if guess ** 2 > num:
        high = guess
      else:
        low = guess
      guess = (low + high) / 2
    print("Approximate square root of {} is {}".format(num, guess))
  else:
    print("Cannot find square root for negative integer")
