import sys

def solve(num):
  ret = ""
  numbers = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
  numerals = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']


  i = len(numbers) - 1
  while num > 0:
    if num >= numbers[i]:
      num -= numbers[i]
      ret += numerals[i]
    else:
      i -= 1
  
  return ret

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Usage: python leetle.py <number>")
    sys.exit(1)

  try:
    num = int(sys.argv[1])
    if num <= 0:
      raise ValueError
    print(solve(num))
  except ValueError:
    print("Only positive integers.")
    sys.exit(1)