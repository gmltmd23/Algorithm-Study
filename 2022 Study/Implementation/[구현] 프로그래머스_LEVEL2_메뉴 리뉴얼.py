from itertools import combinations

def solution(orders, course):
    courseMap = {}
    for nowOrder in orders:
        for courseMenuCount in course:
            for courseMenu in list(combinations(sorted(nowOrder), courseMenuCount)):
                if courseMenu not in courseMap:
                    courseMap[courseMenu] = 0
                courseMap[courseMenu] += 1

    finalCourseMenuMap = {}
    for courseMenu in courseMap:
        if courseMap[courseMenu] >= 2:
            if len(courseMenu) not in finalCourseMenuMap:
                finalCourseMenuMap[len(courseMenu)] = []
            finalCourseMenuMap[len(courseMenu)].append((courseMap[courseMenu], courseMenu))

    answer = []
    for courseMenuCount in finalCourseMenuMap:
        courseMenuList = sorted(finalCourseMenuMap[courseMenuCount], key = lambda x: -x[0])
        maximumPerson = courseMenuList[0][0]
        for nowPerson, courseMenu in courseMenuList:
            if maximumPerson == nowPerson:
                answer.append("".join(courseMenu))

    return sorted(answer)


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))