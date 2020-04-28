class Stack:

    def __init__(self) -> None:
        self._list = []

    def isEmpty(self) -> bool:
        return len(self._list) == 0

    def push(self, value: object) -> None:
        self._list.append(value)

    def pop(self) -> object:
        if self.isEmpty():
            return None
        value = self._list[-1]
        self._list = self._list[:-1]
        return value

    def peek(self) -> object:
        if self.isEmpty():
            return None
        return self._list[-1]

    def size(self) -> int:
        return len(self._list)
