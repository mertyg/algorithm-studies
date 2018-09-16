from random import randint


#leetcode.com problem with the same name as the function.
#Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
#simple divide and conquer approach.

def operations(ch,a,b):
    if ch=="+": return a+b
    if ch=="-": return a-b
    else: return a*b

def diffWaysToCompute(input):
    """
    :type input: str
    :rtype: List[int]
    """
    res = list()
    ops = ["+","-","*"]
    if input.isdigit():
        temp = int(input)
        return list([temp])
    else:
        for i in range(len(input)):
            if input[i] in ops:
                left = diffWaysToCompute(input[:i])
                right = diffWaysToCompute(input[i+1:])
                for res1 in left:
                    for res2 in right:
                        res.append(operations(input[i],int(res1),int(res2)))
        return list(res)


#another leetcode question
#calculating the majority element(that is occured in a given array more than length/2 times)
#divide and conquer approach

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums is None:
        return None
    if len(nums)==1:
        return nums[0]
    mid = len(nums)//2
    left = majorityElement(nums[:mid])
    right = majorityElement(nums[mid:])
    return [left,right][nums.count(right)>len(nums)//2]
