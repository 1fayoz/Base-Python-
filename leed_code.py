# Two Sum
"""nums = [2,7,3,15] 
target = 9

for i, element in enumerate(nums):
    for j, son_2 in enumerate(nums):
        if son_2 + element == target and i != j :
            print([i, j])
"""

# polindrom
"""x = 121

a = str(x)

b = a == a[::-1]

print(b)
"""

# 3 chisi comman perfix
"""strs = ["flower","flow","flight"]
strs = sorted(strs, key=len)

results = []
max_prefix = strs[0]
for i in strs: 
    prefex = "" 
    for j in range(len(max_prefix)): 
         if i[j] != max_prefix[j]:
             break
             prefex += i[j]
         results.append(prefex)

if not results:
    print ('')
    
print (min(results))
num = 16"""


#lenth_ of_last_word

"""def length_of_last_word(s):
    words = s.split()

    if len(words) == 0:
        return 0

    return len(words[-1])

s = "Hello World"
result = length_of_last_word(s)
print(result)"""

#plus one


"""digits = [1,2,3]
b = 0
a = len(digits)-1
while b < a:
    digits[a] + 1
    b+=1
    print(digits)"""


# Move zeroes

"""nums = [0, 1, 0, 3, 12]
zeroes = nums.count(0)
for i in range(zeroes):
    nums.remove(0)
    nums.append(0)

print(nums)"""


# power of four

"""def isPowerOfFour(n):
    while n % 4 == 0:
        n /= 4
    return n == 1

print(isPowerOfFour(16))"""

#isjawel in stone

"""def ls_In_Stones(jewels, stones):
    
    count = 0
    for i in stones:
        if i in jewels:
            count += 1
    
    return count

jewels = "aA"
stones = "aAAbbbb"
result = ls_In_Stones(jewels, stones)
print(result)"""


# largest number at least twice of others
"""
def largest_number(nums):
    max_index = nums.index(max(nums))
    for index, value in enumerate(nums):
        if index != max_index and value * 2 > nums(max_index):
                                 
            return -1
        return max_index """

# self division numbers
"""
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left, right+1):
            count = 0
            if "0" in str(i):
                continue
            for j in str(i):
                if i % int(j) != 0:  
                    break
                count += 1
            if count == len(str(i)):
                result.append(i)
        return result"""


# maximum  number of words

"""def maxWords(sentences):
    max_number = 0

    for i in sentences:
        a = i.split()
        count = len(a)
        max_number = max(max_number, count)
    return max_number

sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
result = maxWords(sentences)
print(result)"""
    
#26. Remove Duplicates from Sorted Array

"""class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:  #[1, 1,1,2 ]
        if len(nums) <= 1 or len(set(nums)) == len(nums):
            return len(nums)
        for index, value in enumerate(nums.copy()):
            if index > 0:
                if value in nums[:index] and value != '_':
                    nums[index] = 1000
                    nums.append("_")
        
        while 1000 in nums:
            nums.remove(1000)
        return len(set(nums))-1"""
# roman to int

"""def roman_to_int(s):
    roman_values = {
        'I': 1, 
        'V': 5, 
        'X': 10, 
        'L': 50, 
        'C': 100, 
        'D': 500, 
        'M': 1000
        }
    result = 0

    for i in range(len(s)):
        if i < len(s) - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
            result -= roman_values[s[i]]
        else:
            result += roman_values[s[i]]

    return result
roman_numeral = "CC"
result = roman_to_int(roman_numeral)
print(f"Input: {roman_numeral}\nOutput: {result}")"""

# 20. Valid Parentheses
"""def isValid(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or stack.pop() != brackets[char]:
                return False
        else:
            return False

    return not stack

# Example usage:
input_string = "()"
output = isValid(input_string)
print(output)"""

# 35. Search Insert Position

"""nums = [1,3,5,6]
target = 2 
nums = [1,3,5,6]
target = 5

for index ,value  in enumerate(nums):
    if value == target:
        print( index)
    elif target != value:
        a = target - 1
        b = a == value
        print (b[index])"""
        


"""def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    
    
    while left <= right:
        mid = left + (right - left) // 2
        print(left,right)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # If the target is not found, 'left' will be the index where it should be inserted
    return left

nums = [1, 3, 5, 6]
target = 5
result = search_insert(nums, target)
print(result)
"""




# class Solution(object):
#    def romanToInt(self, s):
#        """
#        :type s: str
#        :rtype: int
#        """
#        translations = {
#       'V' : 5,
#        'X' : 10,
#        'L' : 50,
#        'C' : 100,
#        'D' : 500,
#        'M' : 1000
#        }
#        number = 0
#        s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
#        s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
#        s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
#        for char in s:
#        number += translations[char]
#        return number

def should_i_wear_this_hat(self,hat):
    if not isinstance(hat, Hat):
        return False
    current_fashion = get_fashion()
    weather_outside = self.look_out_of_window()
    is_stylish = self.evaluate_style(hat, current_fashion)
    if weather_outside.is_raining:
        print()















