if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr1 = list(arr)
    arr1.sort(reverse=True)

    i = 0

    while arr1[i] == arr1[i + 1]:
        i = i + 1

    print(arr1[i + 1])
