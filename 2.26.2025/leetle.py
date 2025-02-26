import sys
def solve(s):
  for i in range(len(s)):
    front = s[:i]
    back = s[i+1:]
    new = front + back
    if new == new[::-1]:
      return True
  return False

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Usage: python leetle.py <string>")
    sys.exit(1)

  s = str(sys.argv[1])
  print(solve(s))