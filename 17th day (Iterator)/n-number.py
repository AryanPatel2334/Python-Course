#n numbers

class Counter:
    def __init__(self,n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        else:
            value = self.current
            self.current += 1
            return value

count = Counter(5)
for num in count:
    print(num)
