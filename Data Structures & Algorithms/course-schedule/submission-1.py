class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {course: [] for course in range(numCourses)} # int -> [int]

        for prereq in prerequisites:
            adj[prereq[0]].append(prereq[1])

        course_path = set()

        def dfs(course) -> bool:
            # If course already taken in course path
            if course in course_path:
                return False

            # If course does not have any remaining prereqs
            if len(adj[course]) == 0:
                return True

            # register course on current course path
            course_path.add(course)

            # Do DFS search on each prereq for this course
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
            
            # All prereqs are satisfied so we can safely set prereqs to empty list
            adj[course] = []
            course_path.remove(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True