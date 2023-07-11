nums = [1,2,3]
print(type(nums))

nums.append(3)
print(len(nums))

nums[3] = 100
nums.insert(0, -200)

print(nums[0]) # primeiro elemento
print(nums[-1]) # ultimo elemento
print(nums[-2]) # penultimo elemento

print(nums)