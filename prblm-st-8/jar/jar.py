class Jar:
    def __init__(self, capacity=12):
        # Validate that capacity is a non-negative integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Must deposit a non-negative integer number of cookies.")
        if self._size + n > self._capacity:
            raise ValueError("Deposit would exceed jar capacity.")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Must withdraw a non-negative integer number of cookies.")
        if n > self._size:
            raise ValueError("Not enough cookies to withdraw.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size