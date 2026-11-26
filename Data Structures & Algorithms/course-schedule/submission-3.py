class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = {}
        for a, b in prerequisites:
            if a not in reqs:
                reqs[a] = []
            reqs[a].append(b)
            
        # print(reqs)


        # Notations for status of each node
        NOT_VISITED = 0
        VISITING = 1
        VISITED = 2

        # Starting with all courses not visited yet
        status = [NOT_VISITED for _ in range(numCourses)]




        def dfs(course) -> bool:
            if status[course] == VISITING:
                return False
            
            if status[course] == VISITED:
                return True

            status[course] = VISITING

            to_take = reqs.get(course, [])

            for c in to_take:
                if not dfs(c):
                    return False
            
            status[course] = VISITED
            return True




        for course in range(numCourses):
            if not dfs(course):
                return False



        # Default Case
        return True