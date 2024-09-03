def average(array):
    heights_set = set(array)
    sum_of_heights = sum(heights_set)
    num_of_heights = len(heights_set)
    return sum_of_heights / num_of_heights


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
