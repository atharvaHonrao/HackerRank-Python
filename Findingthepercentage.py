if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    ans = list(student_marks[query_name])

    sum1 = sum(ans)

    avg = float(sum1 / 3)

    print('%.2f' % avg)