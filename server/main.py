import ctypes

class Array:
    def __init__(self):
        self.capacity = 0
        self.size = 0
        self.data = (0 * ctypes.py_object)()

    def resize(self, new_capacity):
        new_data = (new_capacity * ctypes.py_object)()

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity

    def push(self, value):
        if self.size == self.capacity:

            if self.capacity == 0:
                self.resize(1)
            else:
                self.resize(self.capacity * 2)

        self.data[self.size] = value
        self.size += 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        return self.data[index]

    def __str__(self):
        result = "["

        for i in range(self.size):
            result += str(self.data[i])

            if i < self.size - 1:
                result += ", "

        result += "]"
        return result


arr = Array()

arr.push(11)
arr.push(12)
arr.push(13)
arr.push(14)

print(arr)
print(arr.get(0))

