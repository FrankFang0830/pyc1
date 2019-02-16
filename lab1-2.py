ata = [('John', ('Physics', 80)), ('Daniel', ('Science', 90)),
        ('John', ('Science', 95)), ('Mark', ('Maths', 100)),
        ('Daniel', ('History', 75)), ('Mark', ('Social', 95))]


def sort_by_course_name(o1: tuple) -> str:
    return o1[0]


if __name__ == '__main__':
    result = {}
    for element in data:
        person, score = element
        if person in result:
            result[person].append(score)
            result[person].sort(key=sort_by_course_name)
        else:
            result[person] = [score, ]

    print("result = ", result)