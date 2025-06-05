

def two_sum(nums, target):
    num_dict={}
    for i in range(len(nums)):
      complement = target - nums[i]
    if complement in num_dict:
     return[num_dict[complement],i ]
    num_dict[nums[i]]= i 

print(two_sum([2,7 ,11,15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))