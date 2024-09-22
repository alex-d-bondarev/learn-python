import logging

logger = logging.getLogger(__name__)


class MyHashTable:
    LOAD_FACTOR: float = 0.75

    def __init__(self, size=None):
        self.num_of_buckets = size if size else 10
        self.buckets = [[] for _ in range(self.num_of_buckets)]
        self.num_of_values = 0

    @staticmethod
    def _str_hash(value: str) -> int:
        chars_hash = 0
        for char in value:
            chars_hash = chars_hash * 31 + ord(char)

        return chars_hash

    def _hash(self, value) -> int:
        if isinstance(value, str):
            value_hash = self._str_hash(value)
        elif isinstance(value, int):
            value_hash = value
        else:
            msg = (
                f"Only str and int values are supported, "
                f"but the given value type is {type(value)}"
            )
            raise TypeError(msg)

        return value_hash % self.num_of_buckets

    def _rehash(self) -> None:
        logger.debug("Rehashing")
        all_values = self.to_list()
        self.num_of_buckets *= 2
        self.num_of_values = 0

        self.buckets = [[] for _ in range(self.num_of_buckets)]

        for value in all_values:
            self.add(value)

    def contains(self, value) -> bool:
        value_hash = self._hash(value)
        return value in self.buckets[value_hash]

    def add(self, value) -> "MyHashTable":
        value_hash = self._hash(value)
        self.buckets[value_hash].append(value)
        self.num_of_values += 1

        if self._time_to_rehash():
            self._rehash()

        return self

    def _time_to_rehash(self):
        current_load_factor = self.num_of_values / self.num_of_buckets
        msg = f"Current load factor is {current_load_factor}"
        logger.debug(msg)
        return self.num_of_values / self.num_of_buckets > self.LOAD_FACTOR

    def remove(self, value) -> bool:
        value_hash = self._hash(value)
        if value in self.buckets[value_hash]:
            self.buckets[value_hash].remove(value)
            self.num_of_values -= 1
            return True
        return False

    def size(self) -> int:
        return self.num_of_values

    def to_list(self) -> list[str | int]:  # noqa: FA102
        result = list()
        for bucket in self.buckets:
            result += bucket

        return result


def test_empty_hash_table():
    h_table = MyHashTable()

    assert h_table.contains(42) is False, "Hash table is empty"
    assert h_table.remove(42) is False, "Nothing to remove"
    assert h_table.size() == 0, "Empty means that size is 0"
    assert h_table.to_list() == [], "Empty means that list representation is []"


def test_single_element_in_hashtable():
    h_table = MyHashTable()
    h_table.add(42)

    assert h_table.size() == 1, "Not empty any more"
    assert h_table.contains(42) is True, "Hash table not empty"

    non_empty_msg = "Non-empty means that list representation contains its value [42]"
    assert h_table.to_list() == [42], non_empty_msg
    assert h_table.remove(99) is False, "99 was not there, so False for removed"
    assert h_table.remove(42) is True, "42 was there, so True for removed"
    assert h_table.size() == 0, "Empty again"


def test_multiple_elements_in_hashtable():
    h_table = MyHashTable()
    h_table.add(42).add("Bob").add("Alice").add(42).add("Will")

    assert h_table.size() == 5, "Duplicates (42) are also saved"  # noqa: PLR2004
    assert h_table.contains(42) is True, "Hash table not empty"
    assert h_table.to_list() == [42, 42, "Bob", "Alice", "Will"]
    assert h_table.remove(99) is False, "99 was not there, so False for removed"
    assert h_table.remove(42) is True, "42 was there, so True for removed"
    assert h_table.remove("Alice") is True, "Alice was there, so True for removed"
    assert h_table.size() == 3, "2 elements less"  # noqa: PLR2004
    assert h_table.to_list() == [42, "Bob", "Will"]


def test_rehash_doubles_buckets_size():
    double_buckets = 20
    h_table = MyHashTable()
    h_table.add(42).add("Bob").add("Alice").add(42).add("Will")
    h_table.add(0).add(1).add(2).add(3).add(4)

    assert h_table.num_of_buckets == double_buckets


def test_no_rehash_when_initial_size_is_big_enough():
    init_size = 14
    h_table = MyHashTable(init_size)
    h_table.add(42).add("Bob").add("Alice").add(42).add("Will")
    h_table.add(0).add(1).add(2).add(3).add(4)

    assert h_table.num_of_buckets == init_size
