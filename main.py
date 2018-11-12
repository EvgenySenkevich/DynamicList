import ctypes


class DynArray:

    def __init__(self):
        self.count = 0
        self.capasity = 16
        self.array = self.make_array(self.capasity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capasity = new_capacity

    def append(self, itm):
        if self.count == self.capasity:
            self.resize(2*self.capasity)
        self.insert(self.count, itm)

    def insert(self, j, itm):
        if self.count == self.capasity:
            self.resize(2*self.capasity)
        if j < 0 or j > self.count:
            return

        new_array = self.make_array(self.capasity)
        for i in range(j):
            new_array[i] = self.array[i]
        new_array[j] = itm
        self.count += 1
        for i in range(j+1, self.count):
            new_array[i] = self.array[i-1]

        self.array = new_array

    def delete(self, j):
        new_array = self.array
        self.array = self.make_array(self.capasity)
        count = self.count
        self.count = 0
        if self.count <= self.capasity/2 and self.capasity > 16:
            self.resize(self.capasity//2)
        for i in range(count):
            if i != j:
                self.append(new_array[i])


if __name__ == "__main__":
    da = DynArray()
    da.append(1)
    da.append(2)
    da.append(3)
    da.append(4)
    da.append(5)
    for i in range(0, len(da)):
        print(da[i])
