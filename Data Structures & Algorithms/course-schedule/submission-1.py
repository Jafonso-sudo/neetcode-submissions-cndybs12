class Course:
    def __init__(self):
        self.num_req = 0
        self.allows = []

# Note
# - Alternative is to do Cycle detection

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [Course() for _ in range(numCourses)]
        visited = set()
        for course_idx, requirement_idx in prerequisites:
            courses[course_idx].num_req += 1
            courses[requirement_idx].allows.append(courses[course_idx])

        def dfs(course):
            nonlocal numCourses
            if course.num_req or course in visited:
                return
            visited.add(course)
            for neigh in course.allows:
                neigh.num_req -= 1
                dfs(neigh)


        for course in courses:
            dfs(course)
        
        return numCourses - len(visited) == 0