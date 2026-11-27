class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        products = []
        product = 1

        num_zero = 0

        for element in nums: 
            if element != 0:
                product *= element
            else: 
                num_zero +=1

        if num_zero > 1: 
            return [0] * len(nums)

        if 0 in nums: 
            for num in nums: 
                if num == 0: 
                    products.append(int(product))

                else: 
                    products.append(0)

        else:
            for num in nums: 
                products.append(int(product/num))

        return products


        