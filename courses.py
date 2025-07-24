courses = ["MTH 101", "PHY 101", "CHM 101", "CSC 101", "GST 101"]
print(courses)
courses.insert(0, "ENG 101")

print(courses)
courses.remove(courses[-1])
print(courses)
courses.insert(3, "BIO 101")
print(courses)
print(len(courses))
