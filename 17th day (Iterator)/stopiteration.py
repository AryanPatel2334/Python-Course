#try except

fruits = ["apple","banana","orange"]

fruit_iter = iter(fruits)

try:
    print(next(fruit_iter))
    print(next(fruit_iter))
    print(next(fruit_iter))
    print(next(fruit_iter))
except StopIteration:
    print("No more items")

