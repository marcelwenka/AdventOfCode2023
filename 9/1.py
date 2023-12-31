
s = 0
with open("9/data") as file:
    for line in file:
        nums = list(map(int, line.split()))
        extr = nums[-1]
        while not all(n == 0 for n in nums):
            nums = [n2 - n1 for n1, n2 in zip(nums[:-1], nums[1:])]
            extr += nums[-1]
        s += extr
print(s)
