# two sum, u have an array of numbers and also u have a target
# question is find any 2 numbers that add up to the target, then return their index
# time complexity < O(n^2)
# example num = [1, 2, 3, 4]  target = 7  answer =  [2, 3]
# so here we are going to use hash-tables
# key = index number = value
# i store the key value after i checked the difference

num = [1, 2, 3, 4]
target = 7

def twosum(num, target):
    dif = {}
    for i in range(len(num)):
        diff = target - num[i]
        if diff in dif:
            return [dif[diff], i]
        dif[num[i]] = i
    return []

answer = twosum(num, target)
print(answer)

# when implemented in leetcode this was the code i used
class Solution(object):
    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """

        sum = {}
        for number in range(len(nums)):
            diff = target - nums[number]
            if diff in sum:  # if the diff is inside the sum, this works for only
# searching key inside sum, it wont work if it is value inside the sum
# so here diff(key) inside the sum
                return [sum[diff], number]
            else:
                sum[nums[number]] = number
                

