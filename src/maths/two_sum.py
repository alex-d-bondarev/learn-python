from typing import List


class InitialSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = last = len(nums) - 1
        found = False
        while not found:
            if nums[start] + nums[end] == target:
                found = True
            else:
                end -= 1
                if start == end:
                    start += 1
                    end = last

        return [start, end]


class BetterSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for index, value in enumerate(nums):
            expected = target - value
            if expected in seen:
                return [seen[expected], index]
            else:
                seen[value] = index
        return [-1, -1]  # unexpected input


def test_2_same_numbers():
    nums = [1, 1]
    target = 2
    expected = [0, 1]
    assert InitialSolution().twoSum(nums, target) == expected
    assert BetterSolution().twoSum(nums, target) == expected


def test_2_different_numbers():
    nums = [1, 2]
    target = 3
    expected = [0, 1]
    assert InitialSolution().twoSum(nums, target) == expected
    assert BetterSolution().twoSum(nums, target) == expected


def test_with_3_numbers():
    nums = [1, 2, 3]
    target = 5
    expected = [1, 2]
    assert InitialSolution().twoSum(nums, target) == expected
    assert BetterSolution().twoSum(nums, target) == expected


def test_example_1():
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    assert InitialSolution().twoSum(nums, target) == expected
    assert BetterSolution().twoSum(nums, target) == expected


def test_example_2():
    nums = [3, 2, 4]
    target = 6
    expected = [1, 2]
    assert InitialSolution().twoSum(nums, target) == expected
    assert BetterSolution().twoSum(nums, target) == expected


def test_example_3():
    nums = [3, 3]
    target = 6
    expected = [0, 1]
    assert InitialSolution().twoSum(nums, target) == expected
    assert BetterSolution().twoSum(nums, target) == expected
