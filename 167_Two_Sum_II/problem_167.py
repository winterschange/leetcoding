import json

class Solution:
    def binarySearch(self, nums, target, low, up):
        while low <= up:
            mid = int((low + up) / 2)
            if target >  nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                up = mid - 1
            else:
                return mid
        else:
            return up

    def twoSum(self, nums, target):
        up = len(nums)-1
        low = 0
        while nums[low] + nums[up] != target:
            up = self.binarySearch(nums, target - nums[low], low+1, up)
            if nums[low] + nums[up] == target:
                break
            else:
                low += 1

        return low+1, up+1

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            numbers = stringToIntegerList(line);
            line = next(lines)
            target = int(line);

            ret = Solution().twoSum(numbers, target)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
