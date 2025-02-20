def solve(nums):
    count1 = 0
    count2 = 0
    num1 = None
    num2 = None

    if len(nums) < 3:
        return nums

    for num in nums:

        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1
        elif count1 == 0:
            num1 = num
            count1 = 1
        elif count2 == 0:
            num2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    
    ret = []
    count1 = count2 = 0
    for num in nums:
        if num == num1:
            count1 += 1
        elif num == num2:
            count2 += 1

    if count1 > len(nums)//3:
        ret.append(num1)
    if count2 > len(nums)//3:
        ret.append(num2)
    
    return ret

if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(solve(nums))