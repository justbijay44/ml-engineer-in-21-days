nums = [2, 7, 11, 22]

def two_sum(nums, target):
    dict_ = {}
    for idx, num in enumerate(nums):
        compliment = target - num
        if compliment in dict_:
            return [dict_[compliment], idx]
        
        dict_[num] = idx

    return []

print(two_sum(nums, 9))
print(two_sum([3, 2, 4], 4))