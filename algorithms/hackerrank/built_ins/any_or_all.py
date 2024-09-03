if __name__ == '__main__':
    _ = input()
    values = input().split()
    print(
        all(int(n) > 0 for n in values) and any(n == n[::-1] for n in values)
    )
