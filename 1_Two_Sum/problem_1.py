import json

class Solution:
    # find the position of target or the number just small than target
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
                    
           
    #def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        '''
        # the o(n^2) algorithm
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j 
        '''
        
        # '''
        # if the list is not sortted, sort it 
        r = dict(sorted(dict(enumerate(nums)).items(), key=lambda x:x[1]))
        nums_sortted = list(r.values())
        index_sortted =  list(r.keys())

        up = len(nums)-1
        low = 0 
        while nums_sortted[low] + nums_sortted[up] != target:
            up = self.binarySearch(nums_sortted, target - nums_sortted[low], low+1, up)
            if nums_sortted[low] + nums_sortted[up] == target:
                break
            else:
                low += 1
        if index_sortted[low] < index_sortted[up]:
            return index_sortted[low], index_sortted[up] 
        else:  
            return index_sortted[up], index_sortted[low]
        '''
        # hash_map
        num_map = {}
        for i, v in enumerate(nums):
            j = num_map.get(target - v)
            if j is not None and i != j:
                return [j, i]
            num_map[v] = i

        return []
        '''

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
            nums = stringToIntegerList(line);
            line = next(lines)
            target = int(line);
            
            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
