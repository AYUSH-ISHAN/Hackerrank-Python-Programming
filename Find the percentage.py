if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # print(student_marks)   it is a dictionary
    # print(len(student_marks))   gives the  length of the dictionary
    name_marks = []
    for i in range(len(student_marks)):
        if student_marks[query_name]:
            name_marks.append(student_marks[query_name])
            full = sum(name_marks[0])
            average = full / 3
            print('%.2f' % average)
            break
    # print(name_marks)
