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
            raise  IndexError('Index is out of bounds')
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
        self.array[self.count] = itm
        self.count += 1


if __name__ == "__main__":
    da = DynArray()
    for i in range(64):
        da.append(i)
        print(da[i])