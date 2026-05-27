class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Calculate left products
        left_products = [1]
        product_so_far = 1
        for num in nums[:-1]:
            product_so_far *= num
            left_products.append(product_so_far)
        

        # Calculate right products
        right_products = [1]
        product_so_far = 1
        for num in nums[::-1][:-1]:
            product_so_far *= num
            right_products.append(product_so_far)   

        right_products = right_products[::-1]

        final_products = []
        for i in range(len(left_products)):
            final_products.append(left_products[i] * right_products[i])

        return final_products
