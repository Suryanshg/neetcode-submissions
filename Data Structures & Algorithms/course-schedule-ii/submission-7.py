class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre_map = {}
        for a, b in prerequisites:
            if a not in pre_map:
                pre_map[a] = []
            pre_map[a].append(b)

        NOT_VISITED = 0
        VISITING = 1
        VISITED = 2

        status = [NOT_VISITED for _ in range(numCourses)]


        order = []

        def dfs(course):
            if status[course] == VISITING:
                return False
            
            if status[course] == VISITED:
                return True

            status[course] = VISITING
            reqs = pre_map.get(course, [])

            for c in reqs:
                if not dfs(c):
                    return False
            
            order.append(course)

            status[course] = VISITED

            return True


        for course in range(numCourses):
            if not dfs(course):
                return []

        return order