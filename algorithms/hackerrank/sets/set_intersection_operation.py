if __name__ == '__main__':
    english_subscribers_amount = input()
    english_subscribers = set(map(int, input().split()))
    french_subscribers_amount = input()
    french_subscribers = set(map(int, input().split()))

    print(len(english_subscribers.intersection(french_subscribers)))
