import logging

logger = logging.getLogger(__name__)


class MyHashMap:
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __repr__(self):
            return f"Entry({repr(self.key)}, {repr(self.value)})"

    LOAD_FACTOR: float = 0.75

    def __init__(self, size=None):
        self.num_of_buckets = size if size else 10
        self.buckets: list[list["MyHashMap.Entry"]] = [[] for _ in range(self.num_of_buckets)]
        self.num_of_entries = 0

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
            value_hash = hash(value)

        return value_hash % self.num_of_buckets

    def _rehash(self) -> None:
        logger.debug("Rehashing")
        all_entries = self.to_list()
        self.num_of_buckets *= 2
        self.num_of_entries = 0

        self.buckets = [[] for _ in range(self.num_of_buckets)]

        for entry in all_entries:
            self.put(entry.key, entry.value)

    def put(self, key, value) -> None:
        key_hash = self._hash(key)
        new_entry = self.Entry(key, value)
        bucket = self.buckets[key_hash]
        updated = False

        for entry in bucket:
            if entry.key == key:
                entry.value = value
                updated = True

        if not updated:
            self.buckets[key_hash].append(new_entry)
            self.num_of_entries += 1

            if self._time_to_rehash():
                self._rehash()

    def _time_to_rehash(self):
        current_load_factor = self.num_of_entries / self.num_of_buckets
        msg = f"Current load factor is {current_load_factor}"
        logger.debug(msg)
        return self.num_of_entries / self.num_of_buckets > self.LOAD_FACTOR

    def remove(self, key) -> bool:
        value_hash = self._hash(key)
        bucket = self.buckets[value_hash]
        for index, entry in enumerate(bucket):
            if entry.key == key:
                bucket.pop(index)
                self.num_of_entries -= 1
                return True
        return False

    def size(self) -> int:
        return self.num_of_entries

    def to_list(self) -> list["MyHashMap.Entry"]:  # noqa: FA102
        result = list()
        for bucket in self.buckets:
            for entry in bucket:
                result.append(entry)

        return result

    def get(self, key):
        value_hash = self._hash(key)
        bucket = self.buckets[value_hash]
        for index, entry in enumerate(bucket):
            if entry.key == key:
                return bucket[index].value
        return None


def test_hash_map_flow():
    h_map = MyHashMap()

    assert h_map.size() == 0, "Empty from the start"

    h_map.put("duplicate", 42)
    h_map.put("duplicate", 42)
    assert h_map.remove("none") is False
    assert h_map.size() == 1, "No duplicates"

    h_map.put("temp", 99)
    assert h_map.get("temp") == 99
    assert h_map.size() == 2, "Should increment"

    assert h_map.remove("temp") is True
    assert h_map.size() == 1, "Should decrement after deletion"
