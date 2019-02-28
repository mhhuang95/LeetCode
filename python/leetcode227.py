class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip().split()
        s = ''.join(s)
        oper = []
        nums = []
        ls = len(s)
        i,j = 0,0
        while i < ls:
            if s[i] in ['+','-','*','/']:
                nums.append(int(s[j:i]))
                oper.append(s[i])
                j = i+1

            if i == ls-1:
                nums.append(int(s[j:i+1]))
            i += 1
        ls = len(nums)
        i = 1
        while i < ls:
            if oper[i-1] == '-':
                nums[i] *= -1
                i+=1
            elif oper[i-1] == '*':
                nums[i-1] *= nums[i]
                nums.pop(i)
                oper.pop(i-1)
                ls-=1
            elif oper[i-1] == '/':
                if nums[i-1] > 0:
                    nums[i-1] = nums[i-1]//nums[i]
                else:
                    nums[i-1] = -((-nums[i-1])//nums[i])
                nums.pop(i)
                oper.pop(i-1)
                ls-=1
            else:
                i+=1
        return sum(nums)

if __name__ == "__main__":
    s = Solution()
    print(s.calculate("14-3/2"))

