class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        num_ints = len(arr)
        goal = num_ints // 2
        count_dict = dict()
        min_size = 0

        count_dict = collections.Counter(arr)    
        counts = count_dict.values()
        
        max_val = max(counts)
        count_sort_arr = [0]*(max_val+1)
        for x in counts:
          count_sort_arr[x] += 1
        x = len(count_sort_arr)-1
        while x > 0:
          while (count_sort_arr[x] > 0):
            num_ints -= x
            min_size += 1
            count_sort_arr[x] -= 1
            if num_ints <= goal:
              return min_size
          x -=1
          