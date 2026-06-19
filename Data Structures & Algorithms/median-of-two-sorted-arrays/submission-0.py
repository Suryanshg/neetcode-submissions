class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Determine A and B
        # A is the shorter of the two arrays by len
        # The algo below performs binary search on A
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        # Determine the total and half
        total = len(A) + len(B)
        half = total // 2


        # Binary Search on A
        l = 0
        r = len(A) - 1
        while True:
            # Idx of mid ptr of A
            midA = (l + r) // 2 
            
            # Idx of mid ptr of B
            # (midA + 1) is num of elements in left partition of A
            # - 1 in the end converts num of elements in left partition of B into idx
            midB = half - (midA + 1) - 1

            # Determine 
            # Aleft: rightmost of the left part of A
            # Aright: leftmost of the right part of A
            # Bleft: rightmost of the left part of B
            # Bright: leftmost of the right part of B
            # Using "infinity" for cases when mid ptrs go out of bounds
            Aleft = A[midA] if midA >= 0 else float("-infinity")
            Aright = A[midA + 1] if (midA + 1) < len(A) else float("infinity")
            Bleft = B[midB] if midB >= 0 else float("-infinity")
            Bright = B[midB + 1] if (midB + 1) < len(B) else float("infinity")

            # If we found the global left partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)

            elif Aleft > Bright:
                r = midA - 1

            else:
                l = midA + 1
        