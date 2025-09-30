class Counter:
    def __init__(self,start,end):
        self.current = start
        self.end = end


    def __iter__(self):
        return self


    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

#Use the custom iterator

for num in Counter(1,5):
    print(num)
