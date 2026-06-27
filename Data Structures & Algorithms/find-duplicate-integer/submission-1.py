class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        This is a Linked List cycle problem and it utilizes
        Floyd's algorithm to detect where the cycle begins.

        Treat the nums list as a LL where each value is the idx of the
        next pointer.

        Floyd's algo:
        1. Use Slow and Fast pointers and find an intersection point within a 
        cyclic LL
        2. Using intersection point as Slow1 and starting position as Slow2, 
        we move pointers again, until we find a new intersection point for 
        Slow1 and Slow2. This point will be the start of the cycle of
        the LL.

        For proof of Floyd's algo, see:
        https://www.youtube.com/watch?v=wjYnzkAhcNk&t=5s
        """
        # Init fast and slow
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Found intersection point
        # Init slow2
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        return slow

        