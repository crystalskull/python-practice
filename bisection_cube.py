#!/usr/local/bin/python3
'''
Program to find cube root of a number using bisection
search method.
'''
if __name__ == '__main__':
  num = int(input("Enter a number:"))
  epsilon = 0.00001
  low = min(0, num)
  high = max(1, num)
  guess = (low + high) / 2
  while abs(guess ** 3 - num) > epsilon:
    print(low, high, guess)
    if guess ** 3 > num:
      high = guess
    else:
      low = guess
    guess = (low + high) / 2
  print("Approximate cube root of {} is {}".format(num, guess))
