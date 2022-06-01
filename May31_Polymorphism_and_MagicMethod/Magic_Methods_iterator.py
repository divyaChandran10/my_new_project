class NumberSequence:

    def __init__(self, limit=100):
        self.counter = 0
        self.limit = limit

    def __iter__(self):
        #return iter([1, 2, 3, 4, 5])
        return self

    def __next__(self):
        if self.counter > self.limit:
            raise StopIteration()

        self.counter += 1
        return self.counter


if __name__ == '__main__':

    sequence = NumberSequence(limit=10)

    for num in sequence:
        print(num)



