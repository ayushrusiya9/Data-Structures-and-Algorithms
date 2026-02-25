def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(1,len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i,j]

print(two_sum([1,7,11,2],9))

def two_sum_hashmap(numbers, target):
    seen = {}
    for index,num in enumerate(numbers):
        need = target - num 
        if need in seen:
            return [seen[need],index]
        seen[num] = index
    return []

print(two_sum_hashmap([1,7,11,2],9))