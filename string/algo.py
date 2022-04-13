#nums = {4,3,2,1}


def printDigit(nums, k):
    result = []

    def backtrack(start, subRes):
        if len(subRes) == k:
            result.append(subRes.copy())
        if len(subRes) > k:
            return

        for i in range(len(nums)):
            if nums[i] in subRes:
                continue
            subRes.append(nums[i])
            backtrack(i+1, subRes)
            subRes.pop()

    backtrack(0, [])
            
    return result

print(printDigit([4,3,2,1], 3))