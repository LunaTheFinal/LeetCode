class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
       dict_index = {}
       for index, n in enumerate(num):
           dict_index[str(n)] = index 

       for index, n in enumerate(num):
           search_n = target - n
           if dict_index.has_key(str(search_n)):
               if dict_index[str(search_n)] > index:
                   return (index+1,dict_index[str(search_n)]+1)
