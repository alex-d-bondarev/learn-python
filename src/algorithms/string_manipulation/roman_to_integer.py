class Solution:
    def romanToInt_full_mapping(self, s: str) -> int:
        roman_mapping = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
        }

        result = 0
        index = 0
        str_len = len(s)

        while index < str_len:
            if index + 2 <= str_len and s[index:index + 2] in roman_mapping:
                result += roman_mapping[s[index:index + 2]]
                index += 2
            else:
                result += roman_mapping[s[index:index + 1]]
                index += 1

        return result

    def romanToInt_short_mapping(self, s: str) -> int:
        roman_mapping = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
        }

        result, index = 0, 0
        str_len = len(s)

        while index < str_len:
            if index + 1 < str_len:
                if roman_mapping[s[index]] > roman_mapping[s[index + 1]]:
                    result += roman_mapping[s[index]]
                    index += 1
                elif roman_mapping[s[index]] < roman_mapping[s[index + 1]]:
                    result += roman_mapping[s[index + 1]] - roman_mapping[s[index]]
                    index += 2
                else:
                    result += roman_mapping[s[index]]
                    index += 1
            else:
                result += roman_mapping[s[index]]
                index += 1

        return result


def test_single_numbers():
    sol = Solution()
    assert sol.romanToInt_full_mapping('I') == 1
    assert sol.romanToInt_full_mapping('V') == 5
    assert sol.romanToInt_full_mapping('X') == 10
    assert sol.romanToInt_full_mapping('L') == 50
    assert sol.romanToInt_full_mapping('C') == 100
    assert sol.romanToInt_full_mapping('D') == 500
    assert sol.romanToInt_full_mapping('M') == 1000


def test_pair_numbers():
    sol = Solution()
    assert sol.romanToInt_full_mapping('IV') == 4
    assert sol.romanToInt_full_mapping('IX') == 9
    assert sol.romanToInt_full_mapping('XL') == 40
    assert sol.romanToInt_full_mapping('XC') == 90
    assert sol.romanToInt_full_mapping('CD') == 400
    assert sol.romanToInt_full_mapping('CM') == 900


def test_examples():
    sol = Solution()
    assert sol.romanToInt_full_mapping('III') == 3
    assert sol.romanToInt_full_mapping('LVIII') == 58
    assert sol.romanToInt_full_mapping('MCMXCIV') == 1994


def test_single_numbers_v2():
    sol = Solution()
    assert sol.romanToInt_short_mapping('I') == 1
    assert sol.romanToInt_short_mapping('V') == 5
    assert sol.romanToInt_short_mapping('X') == 10
    assert sol.romanToInt_short_mapping('L') == 50
    assert sol.romanToInt_short_mapping('C') == 100
    assert sol.romanToInt_short_mapping('D') == 500
    assert sol.romanToInt_short_mapping('M') == 1000


def test_pair_numbers_v2():
    sol = Solution()
    assert sol.romanToInt_short_mapping('IV') == 4
    assert sol.romanToInt_short_mapping('IX') == 9
    assert sol.romanToInt_short_mapping('XL') == 40
    assert sol.romanToInt_short_mapping('XC') == 90
    assert sol.romanToInt_short_mapping('CD') == 400
    assert sol.romanToInt_short_mapping('CM') == 900


def test_examples_v2():
    sol = Solution()
    assert sol.romanToInt_short_mapping('III') == 3
    assert sol.romanToInt_short_mapping('LVIII') == 58
    assert sol.romanToInt_short_mapping('MCMXCIV') == 1994
