class Solution:
    def splitArray(self, nums, k: int) -> int:
        # Definindo o criterio inicial de busca
        max_element = max(nums)
        sum_reference = sum(nums)
                
        while max_element < sum_reference:
            h = (max_element + sum_reference) // 2 # Estimativa inicial da soma

            sub_arrays = 1
            current_sum = 0
            
            for i in range(len(nums)):
                if current_sum + nums[i] > h:
                    sub_arrays += 1
                    current_sum = nums[i]
                else:
                    current_sum += nums[i]
                    
            # Alterando o criterio de busca de acordo com k
            if sub_arrays > k:
                # Busca com uma soma maior
                max_element = h + 1 
            else:
                # busca com uma soma menor que a atual
                sum_reference = h
        
        return max_element
    
# sol = Solution()

# nums = [7,2,5,10,8]
# k = 2

# max_sum = sol.splitArray(nums, k)

# print(max_sum)
                
                    
                    