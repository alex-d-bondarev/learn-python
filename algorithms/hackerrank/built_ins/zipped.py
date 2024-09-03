if __name__ == '__main__':
    _, X = input().split()
    subjects = list()

    for _ in range(int(X)):
        subjects.append(map(float, input().split()))

    for i in zip(*subjects):
        print("{0:.1f}".format(sum(i)/len(i)))
