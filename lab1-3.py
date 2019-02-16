PythonStudents = ["Zhang Hao", "Fang peihao", "Chen", "Ray", ]
WebApplicationStudents = ["Zhang Hao", "Fang peihao", "Louis", "Frank"]

pySet = set(PythonStudents)
appSet = set(WebApplicationStudents)

# Find the students who are attending both classes
print(pySet & appSet)
print(" are the students attending both classes")

# Find the students who are not attending both classes
print(pySet ^ appSet)
print(" are the students not attending both classes")