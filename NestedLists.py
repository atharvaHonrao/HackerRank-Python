if __name__ == '__main__':

    list1 = list([])
    list2 = list([])

    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name, score])
        list2.append(score)

    list1.sort()
    list2.sort(reverse=False)

    i = 0

    while list2[i] == list2[i + 1]:
        i = i + 1

    small = list2[i + 1]

    for i in list1:
        if i[1] == small:
            print(i[0])





