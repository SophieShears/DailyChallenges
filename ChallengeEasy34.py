nums = []
for i in range(3):
    nums.append(int(raw_input("enter a number: ")))
newnum = sorted(nums)

print((newnum[1]**2)*(newnum[2]**2))