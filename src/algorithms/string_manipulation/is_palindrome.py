class Solution:
    def isPalindrome_int(self, x: int) -> bool:
        num_copy = x
        reversed_num = 0

        while num_copy > 0:
            reversed_num = reversed_num * 10 + num_copy % 10
            num_copy = num_copy // 10

        return x == reversed_num

    def isPalindrome_str(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

    def isPalindrome_str_v2(self, x: int) -> bool:  # The slowest
        return str(x) == ''.join(reversed(str(x)))

    def isPalindrome_pointers(self, x: int) -> bool:  # The fastest
        x_str = str(x)
        start = 0
        stop = len(x_str) - 1

        while True:
            if x_str[start] != x_str[stop]:
                return False

            start += 1
            stop -= 1

            if start > stop:
                break

        return True


def test_int_solution():
    sol = Solution()

    assert sol.isPalindrome_int(1)
    assert sol.isPalindrome_int(121)

    assert not sol.isPalindrome_int(-121)
    assert not sol.isPalindrome_int(10)


def test_str_solution():
    sol = Solution()

    assert sol.isPalindrome_str(1)
    assert sol.isPalindrome_str(121)

    assert not sol.isPalindrome_str(-121)
    assert not sol.isPalindrome_str(10)


def test_str_v2_solution():
    sol = Solution()

    assert sol.isPalindrome_str_v2(1)
    assert sol.isPalindrome_str_v2(121)

    assert not sol.isPalindrome_str_v2(-121)
    assert not sol.isPalindrome_str_v2(10)


def test_pointers_solution():
    sol = Solution()

    assert sol.isPalindrome_pointers(1)
    assert sol.isPalindrome_pointers(121)

    assert not sol.isPalindrome_pointers(-121)
    assert not sol.isPalindrome_pointers(10)
