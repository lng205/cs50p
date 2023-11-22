class Jar():
    def __init__(self, capacity=12) -> None:
        self.capacity = capacity
        self.size = 0
    
    def __str__(self) -> str:
        return "🍪" * self.size
    
    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, n):
        if n < 0:
            raise ValueError
        self._capacity = n

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, n):
        if n < 0 or n > self.capacity:
            raise ValueError
        self._size = n