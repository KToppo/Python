class Fibonacci:
    def __init__(self, limit):
        # default constructor
        self.previous = 0
        self.current = 1
        self.n = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.limit:
            result = self.previous + self.current
            self.previous = self.current
            self.current = result
            self.n += 1
            return result
        else:
            raise StopIteration


# init the fib_iterator
fib_iterator = iter(Fibonacci(10))
while True:
    # print the value of next fibonacci up to 5th fibonacci
    try:
        print(next(fib_iterator))
    except StopIteration:
        break

def sebonachie_series(limit):
    F_1 = 0
    F_2 = 1
    for i in range(limit):
        Fn = F_1 + F_2
        print(Fn)
        F_1 = F_2
        F_2 = Fn
        # F_2 = F_1_cp + F_2_cp
        

sebonachie_series(50)