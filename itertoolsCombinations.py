# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

if __name__ == '__main__':

    strin, k = input().split()
    string = list(strin)
    string.sort()
    j = int(k)

    list1 = list([])  # = (list(combinations(string,1)))

    for i in range(1, j + 1):
        list1 = list1 + ((list(combinations(string, i))))

    for i in list1:
        print("".join(list(i)))






