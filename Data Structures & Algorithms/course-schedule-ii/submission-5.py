class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build Adjacency List
        adj = {course:[] for course in range(numCourses)} # course -> [prereqs]

        for prereq in prerequisites:
            adj[prereq[0]].append(prereq[1])

        taken = set()
        taken_order = []
        course_path = set()

        # DFS styled way of finding if we can take a course
        def can_take(course):
            # If already taken on the current path, then return False
            if course in course_path:
                return False

            # If has no prereqs, then return True
            if course in taken:
                return True

            # Otherwise, add course on the course_path
            course_path.add(course)

            # Check for its prereqs
            for prereq_course in adj[course]:
                if not can_take(prereq_course):
                    return False

            # Means we can take all prereqs safely
            # Remove course from course path and empty out its requirements
            course_path.remove(course)
            adj[course] = []

            # Add this course in taken order
            taken_order.append(course)
            taken.add(course)

            return True

            
        for course in range(numCourses):
            if not can_take(course):
                return []

        return taken_order