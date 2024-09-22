import logging

from dsa.structures.my_hash_table import MyHashTable

logger = logging.getLogger(__name__)


class MyHashSet(MyHashTable):
    LOAD_FACTOR: float = 0.75

    def __init__(self, size=None):
        super().__init__(size)

    def add(self, value) -> "MyHashTable":
        if self.contains(value):
            return self
        else:
            return super().add(value)


def test_empty_hash_table():
    h_set = MyHashSet()

    assert h_set.contains(42) is False, "Hash table is empty"
    assert h_set.remove(42) is False, "Nothing to remove"
    assert h_set.size() == 0, "Empty means that size is 0"
    assert h_set.to_list() == [], "Empty means that list representation is []"


def test_single_element_in_hashtable():
    h_set = MyHashSet()
    h_set.add(42)

    assert h_set.size() == 1, "Not empty any more"
    assert h_set.contains(42) is True, "Hash table not empty"

    non_empty_msg = "Non-empty means that list representation contains its value [42]"
    assert h_set.to_list() == [42], non_empty_msg
    assert h_set.remove(99) is False, "99 was not there, so False for removed"
    assert h_set.remove(42) is True, "42 was there, so True for removed"
    assert h_set.size() == 0, "Empty again"


def test_multiple_elements_in_hashtable():
    h_set = MyHashSet()
    h_set.add(42).add("Bob").add("Alice").add(42).add("Will")

    assert h_set.size() == 4, "Duplicates (42) are not saved"  # noqa: PLR2004
    assert h_set.contains(42) is True, "Hash table not empty"
    assert h_set.to_list() == [42, "Bob", "Alice", "Will"]
    assert h_set.remove(99) is False, "99 was not there, so False for removed"
    assert h_set.remove(42) is True, "42 was there, so True for removed"
    assert h_set.remove("Alice") is True, "Alice was there, so True for removed"
    assert h_set.size() == 2, "2 elements less"  # noqa: PLR2004
    assert h_set.to_list() == ["Bob", "Will"]


def test_rehash_doubles_buckets_size():
    double_buckets = 20
    h_set = MyHashSet()
    h_set.add(42).add("Bob").add("Alice").add(42).add("Will")
    h_set.add(0).add(1).add(2).add(3).add(4)

    assert h_set.num_of_buckets == double_buckets


def test_no_rehash_when_initial_size_is_big_enough():
    init_size = 14
    h_set = MyHashSet(init_size)
    h_set.add(42).add("Bob").add("Alice").add(42).add("Will")
    h_set.add(0).add(1).add(2).add(3).add(4)

    assert h_set.num_of_buckets == init_size
