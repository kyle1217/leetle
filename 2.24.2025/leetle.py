def solve(nums):
  target = len(nums) - 1
  farthest = 0

  if target < 1:
    return True

  for i in range(target):
    farthest = max(farthest, nums[i] + i)
    if farthest >= target:
      return True
  return False

if __name__ == '__main__':
  nums = [2, 3, 1, 1, 4]
  print(solve(nums))