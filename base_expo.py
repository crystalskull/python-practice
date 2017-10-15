#!/usr/local/bin/python3
'''
Program to check if a given number can be represented in
base ** exponent form.
Condition: 0 < exponent < 6
'''

if __name__ == '__main__':
  MAX_EXPO = 6
  num = int(input("Enter a number: "))
  base = 0
  if len(str(num)) > 10:
    ans = input("Large integer will take some time to compute. Do you want to proceed?")
  else:
    ans = 'y'
  while ans == 'yes' or ans == 'y':
    expo = 1
    while expo < MAX_EXPO and base ** expo < abs(num):
      expo += 1
    
    if expo < MAX_EXPO:
        if base ** expo == abs(num):
          if expo % 2 == 0:
            if num < 0:
              print("{} cannot be represented in base ** expo form".format(num))
            else:
              print("Base:+/-{} Expo:{}".format(base, expo))
          else:
            if num < 0:
              base = base * -1
            print("Base:{} Expo:{}".format(base, expo))
          break
        elif base < (abs(num) // base):
          base += 1
        else:
          print("{} cannot be represented in base ** expo form".format(num))
          break
    else:
      base += 1
